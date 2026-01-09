# Video Edit Instructions

**Created**: 9 January 2026

A test pipeline for converting video recordings into precise code editing instructions.

## Purpose

This repository provides a workflow where:

1. A user records a screencast or video (with or without annotations) describing desired edits to an application
2. The recording is processed by a multimodal AI
3. The AI converts the video content into precise editing instructions for an AI coding agent working in a codebase to implement those edits

## Structure

- `screenshare/` - Converted video files (H.265/HEVC MP4)
- `audio/` - Audio-only extracts (Opus OGG)

## Workflow

1. Record screencast describing desired changes
2. Place original recording in repository
3. Convert to space-efficient format
4. Extract audio for transcription
5. Process with multimodal AI to generate editing instructions
