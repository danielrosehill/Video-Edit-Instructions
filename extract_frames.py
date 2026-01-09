#!/usr/bin/env python3
"""
Extract frames from video at timestamps mentioned in timestamped-instructions.md
and generate a JSON mapping screenshots to editing instructions.
"""

import json
import re
import subprocess
import sys
from pathlib import Path


def parse_timestamp(ts: str) -> float:
    """Convert MM:SS or HH:MM:SS to seconds."""
    parts = ts.split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    elif len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    return 0


def extract_instructions_from_markdown(md_path: Path) -> list[dict]:
    """Parse the timestamped instructions markdown and extract instruction data."""
    content = md_path.read_text()

    instructions = []

    # Match table rows with timestamps and instructions
    # Format: | 02:00 | **Instruction 1: Specs Editability** | Description |
    pattern = r"\|\s*(\d{2}:\d{2})\s*\|\s*\*\*Instruction\s*(\d+):\s*([^*]+)\*\*\s*\|\s*([^|]+)\|"

    for match in re.finditer(pattern, content):
        timestamp = match.group(1)
        instruction_num = int(match.group(2))
        instruction_name = match.group(3).strip()
        description = match.group(4).strip()

        # Create a safe filename from the instruction name
        safe_name = re.sub(r"[^a-zA-Z0-9]+", "_", instruction_name.lower()).strip("_")
        filename = f"{instruction_num:02d}_{safe_name}.jpg"

        instructions.append({
            "instruction_number": instruction_num,
            "instruction_name": instruction_name,
            "description": description,
            "timestamp": timestamp,
            "timestamp_seconds": parse_timestamp(timestamp),
            "screenshot_filename": filename,
            "screenshot_path": f"screenshots/{filename}"
        })

    return sorted(instructions, key=lambda x: x["instruction_number"])


def extract_frame(video_path: Path, timestamp: str, output_path: Path) -> bool:
    """Extract a single frame from video at the given timestamp."""
    cmd = [
        "ffmpeg",
        "-y",  # Overwrite output
        "-ss", f"00:{timestamp}",  # Seek to timestamp
        "-i", str(video_path),
        "-vframes", "1",  # Extract one frame
        "-q:v", "2",  # High quality
        str(output_path)
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"Error extracting frame at {timestamp}: {e}")
        return False


def main():
    repo_root = Path(__file__).parent

    # Paths
    video_path = repo_root / "screenshare" / "2026-01-09_13-05-09.mp4"
    md_path = repo_root / "transcripts" / "processed" / "timestamped-instructions.md"
    screenshots_dir = repo_root / "screenshots"
    output_json = repo_root / "editing_instructions.json"

    # Validate inputs
    if not video_path.exists():
        print(f"Error: Video not found at {video_path}")
        sys.exit(1)

    if not md_path.exists():
        print(f"Error: Markdown not found at {md_path}")
        sys.exit(1)

    # Create screenshots directory
    screenshots_dir.mkdir(exist_ok=True)

    # Parse instructions
    print("Parsing timestamped instructions...")
    instructions = extract_instructions_from_markdown(md_path)
    print(f"Found {len(instructions)} instructions")

    # Extract frames
    print("\nExtracting frames from video...")
    for inst in instructions:
        output_path = screenshots_dir / inst["screenshot_filename"]
        print(f"  [{inst['timestamp']}] {inst['instruction_name']}...", end=" ")

        if extract_frame(video_path, inst["timestamp"], output_path):
            print("✓")
        else:
            print("✗ FAILED")

    # Generate JSON output
    print(f"\nGenerating JSON output to {output_json}...")

    output_data = {
        "source_video": str(video_path.relative_to(repo_root)),
        "source_transcript": str(md_path.relative_to(repo_root)),
        "generated_at": subprocess.run(
            ["date", "-Iseconds"], capture_output=True, text=True
        ).stdout.strip(),
        "instructions": instructions
    }

    output_json.write_text(json.dumps(output_data, indent=2))
    print("Done!")

    # Print summary
    print(f"\nSummary:")
    print(f"  - {len(instructions)} instructions extracted")
    print(f"  - Screenshots saved to: {screenshots_dir}")
    print(f"  - JSON output: {output_json}")


if __name__ == "__main__":
    main()
