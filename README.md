# Video Manager

A simple command-line application to manage your YouTube videos using an SQLite database.

## Features

- List all YouTube videos
- Add a new video
- Update video details
- Delete a video

## Usage

1. **Run the application:**
   ```
   python Video_manager.py
   ```

2. **Follow the on-screen menu:**
   - List all videos
   - Add a video (enter name and time)
   - Update a video (by ID)
   - Delete a video (by ID)
   - Exit the app

## Database

- Uses SQLite (`video_database.db`)
- Table: `Videos` (id, name, time)

## Requirements

- Python 3.x
