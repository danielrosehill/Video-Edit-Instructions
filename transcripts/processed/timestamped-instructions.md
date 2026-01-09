# Homebox UI Instructions with Timestamps

These timestamps are estimated based on content flow in a ~14 minute (849 second) screencast. Use these for extracting reference frames at the points where each instruction is discussed.

---

## Timestamp Reference for Frame Extraction

| Timestamp | Instruction | Description |
|-----------|-------------|-------------|
| 00:00 | Introduction | Purpose of screencast - proving concept for AI video instructions |
| 00:30 | Context | This is a fork of Homebox inventory system |
| 01:00 | Item View Overview | Starting the walkthrough of the item view (most important part) |
| 01:15 | Room Display Check | Verifying room display is correct |
| 01:25 | Location Updater | Testing location update functionality |
| 01:35 | IKEA Sniglar Example | Testing with IKEA Sniglar crib (120x60cm variant) |
| 02:00 | **Instruction 1: Specs Editability** | First friction point - specs should be editable on overview page |
| 02:30 | **Instruction 2: Add Variant Field** | Need new database field 'variant' (VARCHAR 255) for product variants |
| 03:00 | AI Spec Generation Test | Testing the Generate Specs feature with Gemini API |
| 03:20 | **Instruction 3: Fix Spec Save Bug** | "Failed to Save specs" error - bug needs fixing |
| 03:45 | Photo Labels Discussion | Discussing product dimensions photo labeling |
| 04:00 | **Instruction 5: Gallery Pill Labels** | Photos should have pill icons showing type (dimensions, etc.) |
| 04:30 | Upload UI Discussion | Browse Gallery and Camera buttons discussion |
| 05:00 | **Instruction 6: Reorganize Upload UI** | Move upload controls beneath photos card |
| 05:30 | Four-Part Upload Card | Browse, Camera, Upload, Drag and Drop buttons |
| 06:00 | Responsive Breakpoints | Mobile vs desktop upload controls |
| 06:20 | **Instruction 7: Media Card Consistency** | Apply same UI pattern to media card |
| 06:45 | Webcam Feature Validation | Camera/webcam feature is working (accidental test) |
| 07:15 | Specs Edit Mode | Looking at specs in edit version |
| 07:30 | **Instruction 8: Markdown Editor** | Future enhancement - markdown editor for specs (lower priority) |
| 08:00 | AI Spec Override Logic | Discussing human vs AI spec handling |
| 08:20 | **Instruction 4: AI Append Logic** | AI should append after blank line if human spec exists |
| 08:45 | Item Type Discussion | Networking and electrical parameters |
| 09:00 | Type Selector Issue | Can select type on create but cannot update afterward |
| 09:20 | **Instruction 9: Type Selector in Top Bar** | Add Update Type button to top action bar |
| 09:45 | **Instruction 10: Reorganize Top Bar** | Move Generate Specs, Suggest Storage, Giveaway to "Other Actions" |
| 10:15 | Notes Tab Testing | Testing note creation - "delightful" |
| 10:30 | **Instruction 11: Delete Confirmation** | Add confirmation modal for note deletion |
| 10:45 | **Instruction 12: Note Edit Functionality** | Add edit icon and update capability for notes |
| 11:00 | Related Items Tab | Testing related items functionality |
| 11:20 | Related Items Search Issue | "torch, torch, torch for car" - cannot distinguish items |
| 11:40 | **Instruction 13: Enhanced Selection Dropdown** | Show thumbnail, name, manufacturer, asset ID, location in dropdown |
| 12:00 | **Instruction 14: Enhanced Display Card** | Related item cards should show more details |
| 12:20 | **Instruction 15: User-Friendly Messages** | "Remove relation" -> "Remove association", etc. |
| 12:45 | Purchase and Warranty Tab | Testing purchase and warranty information |
| 13:00 | **Instruction 17: Purchase Info in Edit View** | Purchase info visible in View but not Edit mode - fix this |
| 13:20 | **Instruction 18: Currency Selection** | Future enhancement - currency selector (lower priority) |
| 13:35 | **Instruction 16: Show Associated Media** | Display invoice/receipt under Purchase, warranty docs under Warranty |
| 13:50 | **Instruction 19: Tab Reordering** | New order: Overview, Specs, Media, Purchase, Related, Notes |
| 14:00 | Rename Tab | Rename "Purchase and Warranty" to just "Purchase" |

---

## Frame Extraction Commands

To extract frames at these timestamps, use ffmpeg:

```bash
# Extract frame at specific timestamp (example: 2:00 for specs editability)
ffmpeg -ss 00:02:00 -i video.mp4 -vframes 1 -q:v 2 frame_specs_editability.jpg

# Batch extract all instruction frames
ffmpeg -ss 00:02:00 -i video.mp4 -vframes 1 -q:v 2 frames/01_specs_editability.jpg
ffmpeg -ss 00:02:30 -i video.mp4 -vframes 1 -q:v 2 frames/02_variant_field.jpg
ffmpeg -ss 00:03:20 -i video.mp4 -vframes 1 -q:v 2 frames/03_spec_save_bug.jpg
ffmpeg -ss 00:04:00 -i video.mp4 -vframes 1 -q:v 2 frames/05_gallery_pills.jpg
ffmpeg -ss 00:05:00 -i video.mp4 -vframes 1 -q:v 2 frames/06_reorganize_upload.jpg
ffmpeg -ss 00:06:20 -i video.mp4 -vframes 1 -q:v 2 frames/07_media_card.jpg
ffmpeg -ss 00:07:30 -i video.mp4 -vframes 1 -q:v 2 frames/08_markdown_editor.jpg
ffmpeg -ss 00:08:20 -i video.mp4 -vframes 1 -q:v 2 frames/04_ai_append_logic.jpg
ffmpeg -ss 00:09:20 -i video.mp4 -vframes 1 -q:v 2 frames/09_type_selector.jpg
ffmpeg -ss 00:09:45 -i video.mp4 -vframes 1 -q:v 2 frames/10_reorganize_topbar.jpg
ffmpeg -ss 00:10:30 -i video.mp4 -vframes 1 -q:v 2 frames/11_delete_confirmation.jpg
ffmpeg -ss 00:10:45 -i video.mp4 -vframes 1 -q:v 2 frames/12_note_edit.jpg
ffmpeg -ss 00:11:40 -i video.mp4 -vframes 1 -q:v 2 frames/13_enhanced_dropdown.jpg
ffmpeg -ss 00:12:00 -i video.mp4 -vframes 1 -q:v 2 frames/14_display_card.jpg
ffmpeg -ss 00:12:20 -i video.mp4 -vframes 1 -q:v 2 frames/15_user_messages.jpg
ffmpeg -ss 00:13:00 -i video.mp4 -vframes 1 -q:v 2 frames/17_purchase_edit.jpg
ffmpeg -ss 00:13:20 -i video.mp4 -vframes 1 -q:v 2 frames/18_currency.jpg
ffmpeg -ss 00:13:35 -i video.mp4 -vframes 1 -q:v 2 frames/16_associated_media.jpg
ffmpeg -ss 00:13:50 -i video.mp4 -vframes 1 -q:v 2 frames/19_tab_reordering.jpg
```

---

## Key Instruction Timestamps (Quick Reference)

| # | Instruction | Timestamp | MM:SS |
|---|-------------|-----------|-------|
| 1 | Specs Editability | 120s | 02:00 |
| 2 | Add Variant Field | 150s | 02:30 |
| 3 | Fix Spec Save Bug | 200s | 03:20 |
| 4 | AI Append Logic | 500s | 08:20 |
| 5 | Gallery Pill Labels | 240s | 04:00 |
| 6 | Reorganize Upload UI | 300s | 05:00 |
| 7 | Media Card Consistency | 380s | 06:20 |
| 8 | Markdown Editor (Future) | 450s | 07:30 |
| 9 | Type Selector in Top Bar | 560s | 09:20 |
| 10 | Reorganize Top Bar | 585s | 09:45 |
| 11 | Delete Confirmation | 630s | 10:30 |
| 12 | Note Edit Functionality | 645s | 10:45 |
| 13 | Enhanced Selection Dropdown | 700s | 11:40 |
| 14 | Enhanced Display Card | 720s | 12:00 |
| 15 | User-Friendly Messages | 740s | 12:20 |
| 16 | Show Associated Media | 815s | 13:35 |
| 17 | Purchase Info in Edit | 780s | 13:00 |
| 18 | Currency Selection (Future) | 800s | 13:20 |
| 19 | Tab Reordering | 830s | 13:50 |

---

**Note:** These timestamps are estimates based on content analysis of the transcript. The actual video may have slightly different timing. Fine-tune as needed after extracting initial frames.
