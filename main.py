import os
import sys
from urllib.parse import unquote, urlsplit
import whisper
import yt_dlp

print("Initializing Universal Audio & Video Whisper ASR Pipeline...")

raw_input = input("\nEnter YouTube URL or drag & drop audio file: ").strip()

if not raw_input:
    print("Error: No input provided.")
    sys.exit(1)

# Clean terminal quotes and escaped spaces
cleaned_input = raw_input.strip("'\"").replace("\\ ", " ")

# Clean file:// prefix and decode %20 spaces from drag-and-drop
if cleaned_input.startswith("file://"):
    cleaned_input = unquote(urlsplit(cleaned_input).path)

target_audio = ""

# 1. Web URL check
if cleaned_input.startswith("http://") or cleaned_input.startswith("https://"):
    print("Detected URL. Downloading audio stream using yt-dlp...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloaded_audio.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([cleaned_input])
    target_audio = "downloaded_audio.wav"
else:
    target_audio = cleaned_input

# 2. Transcribe
if os.path.exists(target_audio):
    print("Loading OpenAI Whisper model (tiny) into memory...")
    model = whisper.load_model("tiny")

    print(f"Transcribing '{os.path.basename(target_audio)}' using Whisper...")
    result = model.transcribe(target_audio)

    print("\n" + "=" * 50)
    print("TRANSCRIPTION RESULT:")
    print("=" * 50)
    print(result["text"])
    print("=" * 50)
    print("Pipeline execution completed successfully.")
else:
    print(f"Error: Target audio file '{target_audio}' not found.")
