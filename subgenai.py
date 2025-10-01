import os
import subprocess
import sys
import tempfile
import whisper
from whisper.utils import get_writer
from tqdm import tqdm
from datetime import datetime


def log_with_timestamp(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] {message}")


def video_to_subtitles(video_path, output_srt="output.srt", model_size="base", translate=False):
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

        log_with_timestamp(f"[*] Loading Whisper model: {model_size} (this may take time on the first run)...")
        model = whisper.load_model(model_size)

        log_with_timestamp("[*] Transcribing audio...")

        progress_bar = tqdm(total=100, desc="Transcribing", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}]")
        
        result = None
        if translate:
            result = model.transcribe(audio_path, task="translate", verbose=True)
        else:
            result = model.transcribe(audio_path, verbose=True)
        
        progress_bar.n = 100
        progress_bar.last_print_n = 100
        progress_bar.update(0)

        log_with_timestamp(f"[*] Transcription completed.")

        log_with_timestamp(f"[*] Writing subtitles to {output_srt}...")

        srt_writer = get_writer("srt", os.path.dirname(output_srt))

        srt_writer(result, os.path.basename(output_srt), {})

        log_with_timestamp(f"[✔] Done! Subtitles saved at: {output_srt}")

    except Exception as e:
        log_with_timestamp(f"[✖] Error: {str(e)}")

    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)
        if os.path.exists(tmpdir):
            os.rmdir(tmpdir)


if __name__ == "__main__":
    model_size = "base"
    video_file = None
    output_file = "output.srt"
    translate = False

    args = sys.argv[1:]

    if len(args) == 0:
        log_with_timestamp("No arguments provided, using default: --model base")

    i = 0
    while i < len(args):
        if args[i] == "--video":
            if i + 1 < len(args):
                video_file = args[i + 1]
                i += 2
            else:
                log_with_timestamp("Error: '--video' requires a video file path.")
                sys.exit(1)
        elif args[i] == "--model":
            if i + 1 < len(args):
                model_size = args[i + 1]
                i += 2
            else:
                log_with_timestamp("Error: '--model' requires a model size (e.g., 'base', 'small', 'medium', 'large')")
                sys.exit(1)
        elif args[i] == "--output":
            if i + 1 < len(args):
                output_file = args[i + 1]
                i += 2
            else:
                log_with_timestamp("Error: '--output' requires an output file name.")
                sys.exit(1)
        elif args[i] == "--translate":
            translate = True
            i += 1
        else:
            i += 1

    if video_file is None or not os.path.isfile(video_file):
        log_with_timestamp("Error: A valid video file must be provided with '--video'.")
        sys.exit(1)

    if output_file == "output.srt":
        base_name = os.path.splitext(video_file)[0]
        output_file = f"{base_name}.srt"

    video_to_subtitles(video_file, output_file, model_size, translate)
