# 🎬 SUBGEN AI — Subtitle Generator (CLI)

<p align="center">
  <img src="https://raw.githubusercontent.com/nfs-tech-bd/subgenAI/refs/heads/main/Screenshot%202025-10-01%20154442.png" height="400" width="600">
</p>

---

## 🚀 Overview

**SubgenAI** is a lightweight and efficient **command-line tool** that uses **OpenAI's Whisper model** to automatically transcribe and generate subtitles (`.srt`) from video files.  

✨ With a few simple commands, you can:  
- Extract audio from any video  
- Generate accurate subtitles  
- Optionally translate them into **English**  
- Save directly as `.srt` with automatic or custom file naming  

---

## ✨ Features

- 🎯 **Simple CLI** – Run directly from your terminal  
- 📝 **Automatic Naming** – Saves as `video_name.srt` if no output is specified  
- 🌍 **Translate to English** – From any source language  
- ⚡ **Clean & Efficient** – Uses temporary storage and cleans up automatically  
- 🔄 **Flexible Models** – Choose from `tiny`, `base`, `small`, `medium`, `large`  

---

## 🛠️ Tech Stack

- **Language**: Python  
- **Transcription**: OpenAI Whisper  
- **Audio Extraction**: FFmpeg  

---

## 📦 Prerequisites

Before using SubgenAI, make sure you have:

- 🐍 **Python 3.8+**  
- 🎵 **FFmpeg** (required for audio extraction)  

### 🔧 Installation Instructions

- **Windows**: Download from the official [FFmpeg site](https://ffmpeg.org/download.html) and add the `bin` folder to PATH  
- **macOS** (Homebrew):  
  ```bash
  brew install ffmpeg
  ```  
- **Linux** (apt):  
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```  

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/nfs-tech-bd/subgenAI
cd subgenAI
```

### Create and activate a virtual environment (recommended)

**Windows**:
```bash
python -m venv venv
.env\Scriptsctivate
```

**macOS / Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

⚠️ The first time you run the script, Whisper will download the chosen model (default = `base`).  

---

## ▶️ Usage

### Basic (Automatic Output Name)

```bash
python subgenai.py --video "my_video.mp4"
```
👉 Output: `my_video.srt`  

### Specify Output File

```bash
python subgenai.py --video "my_video.mp4" --output "custom_subs.srt"
```

### Choose a Model

```bash
python subgenai.py --video "my_video.mp4" --output "custom_subs.srt" --model "medium"
```

---

## 📊 Model Trade-offs

| Model   | Speed 🚀 | Accuracy 🎯 | Size 💾 |
|---------|----------|-------------|---------|
| tiny    | Fastest  | Lowest      | ~75 MB  |
| base    | Fast     | Medium      | ~142 MB |
| small   | Balanced | Good        | ~466 MB |
| medium  | Slower   | Very Good   | ~1.5 GB |
| large   | Slowest  | Best        | ~3 GB   |

---

## 📜 License

This project is licensed under the **MIT License**.  

---

💡 *Built with ❤️ by <a href="https://t.me/Nafisfuad1">Nafis Fuad</a> with python and a lot of curiosity.*  
