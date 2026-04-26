# batchEditor

A batch processing UI for `auto-editor` to automate silence removal from video files.

## How to Use

### 1. Select a root directory
Click **Select root directory** and choose the folder that contains your video files. The app will recursively scan it and display the number of files found along with their total duration.

### 2. (Optional) Edit selected files
Click **Edit selected files** to open the file list. Use the checkboxes to include or exclude individual videos from the batch before processing starts.

### 3. Configure export options
Switch to the **Configure** tab and choose the NLE you want to export for (Premiere Pro, DaVinci Resolve, etc.) or clip-sequence to export a video file. Set the **margin** to control how many seconds of padding are kept around each loud segment.

### 4. Tune audio thresholds
Click **Configure silence thresholds** to open the multitrack tuner. Each audio stream gets its own slider. Higher values mark more of the audio as silence; lower values are more permissive. Disable a track entirely to exclude it from the silence detection logic.

### 5. (Optional) Save / Load config
Use **Save config** to persist the current settings to a `.txt` file. Use **Load config** later to restore them. This is useful when switching between different recording setups.

### 6. Preview the command
Click **Show command** to see the exact `auto-editor` command that will be run. You can copy it to the clipboard and run it manually if needed.

### 7. Start processing
Click **Start** to open the processing window. A table shows every file with its current status (*Queued*, *Processing*, *Done*, or *Failed*). Hit **Cancel** at any time to stop after the current file finishes. When the batch completes, the window shows a summary with the total number of files processed and the elapsed time.