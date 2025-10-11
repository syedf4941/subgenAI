import os
import subprocess
import sys
import tempfile
import whisper
from whisper.utils import get_writer
from datetime import datetime
import argparse


def log_with_timestamp(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] {message}")


def video_to_subtitles(video_path, output_srt, model_size="base"):
    tmpdir = tempfile.mkdtemp()
    audio_path = os.path.join(tmpdir, "audio.wav")

    try:
        log_with_timestamp("[*] Extracting audio with FFmpeg...")
        ffmpeg_cmd = [
            "ffmpeg", "-y", "-i", video_path,
            "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1",
            audio_path
        ]
        
        subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        log_with_timestamp("[*] Audio extraction completed.")

        log_with_timestamp(f"[*] Loading Whisper model: '{model_size}' (this may take time on the first run)...")
        model = whisper.load_model(model_size)

        log_with_timestamp("[*] Translating audio to English...")
        
        result = model.transcribe(audio_path, task="translate", verbose=False)
        
        log_with_timestamp(f"[*] Translation completed.")

        log_with_timestamp(f"[*] Writing subtitles to {output_srt}...")

        srt_writer = get_writer("srt", os.path.dirname(output_srt))
        srt_writer(result, os.path.basename(output_srt), {})

        log_with_timestamp(f"[✔] Done! Subtitles saved at: {output_srt}")

    except FileNotFoundError:
        log_with_timestamp("[✖] Error: ffmpeg is not installed or not in your PATH. Please install ffmpeg to continue.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        log_with_timestamp(f"[✖] Error during ffmpeg audio extraction: {e.stderr.decode()}")
        sys.exit(1)
    except Exception as e:
        log_with_timestamp(f"[✖] An unexpected error occurred: {str(e)}")
    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)
        if os.path.exists(tmpdir):
            try:
                os.rmdir(tmpdir)
            except OSError as e:
                log_with_timestamp(f"Warning: Could not remove temporary directory {tmpdir}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate English subtitles for a video file using OpenAI's Whisper model.")
    
    parser.add_argument("--video", required=True, help="Path to the video file for subtitle generation.")
    
    parser.add_argument("--model", default="base", help="Whisper model size (e.g., tiny, base, small, medium, large).")
    parser.add_argument("--output", help="Optional path for the output .srt file. Defaults to the same name as the video.")

    args = parser.parse_args()

    output_file = args.output
    if output_file is None:
        base_name = os.path.splitext(args.video)[0]
        output_file = f"{base_name}.srt"
        
    if not os.path.isfile(args.video):
        log_with_timestamp(f"Error: The video file was not found at '{args.video}'")
        sys.exit(1)

    video_to_subtitles(
        video_path=args.video, 
        output_srt=output_file, 
        model_size=args.model
    )

