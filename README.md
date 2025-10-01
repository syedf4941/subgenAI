# SUBGEN AI SUBTITLE GENERATOR (CLI)

A simple and efficient command-line tool that uses OpenAI's Whisper model to automatically transcribe and generate subtitles (.srt files) from any video file.

## Features

- **Simple Command-Line Interface**: Easy to use directly from your terminal.
- **Automatic Naming**: If no output file is specified, it automatically saves the subtitles as `your_video_name.srt`.
- **Translate to English**: Directly translates the transcription from any source language into English.
- **Efficient & Clean**: Uses a temporary directory for audio files and cleans up automatically after processing.
- **Flexible Model Choice**: Easily change the Whisper model size (`tiny`, `base`, `small`, `medium`, `large`) for a trade-off between speed and accuracy.

## Tech Stack

- **Backend**: Python
- **Transcription**: OpenAI Whisper
- **Audio Extraction**: FFmpeg

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8+**
- **FFmpeg**: This is a critical dependency for extracting audio from video.

  ### Installation Instructions:

  - **Windows**: Download from the official website and add the `bin` folder to your system's PATH.
  - **macOS** (using Homebrew): `brew install ffmpeg`
  - **Linux** (using apt): `sudo apt update && sudo apt install ffmpeg`

## Installation & Setup

Follow these steps to get the tool ready for use:

1. Clone the repository:
```
   git clone https://github.com/nfs-tech-bd/subgenAI
```

### Create and activate a virtual environment (recommended):

Windows:
```
python -m venv venv
.\venv\Scripts\activate
  ```

macOS / Linux:
  ```
python3 -m venv venv
source venv/bin/activate
  ```

Install the required Python packages:
  ```
pip install -r requirements.txt
  ```

  - Note: The first time you run the script, Whisper will download the specified model (default is "base"), which may take some time and require a good internet connection.

## Usage

You can run the script from your terminal:

Basic Usage (Automatic Output Name)

This will generate subtitles for my_video.mp4 and save them as my_video.srt.
```
python subgenai.py "my_video.mp4"
```
Specify an Output File Name

This will save the subtitles as custom_subs.srt.
```
python subgenai.py "my_video.mp4" "custom_subs.srt"
```
