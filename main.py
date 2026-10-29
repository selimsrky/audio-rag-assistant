import whisper
import yt_dlp
import os

print("Initializing YouTube Audio Downloader and Whisper ASR Pipeline...")

# Prompt user to input a YouTube URL interactively from the terminal
youtube_url = input("\nEnter the YouTube video URL to transcribe: ").strip()

if not youtube_url:
    print("Error: No URL provided.")
    exit()

# yt-dlp configuration to extract high-quality audio as WAV
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'outtmpl': 'downloaded_audio.%(ext)s',
    'quiet': True
}

print("Downloading audio from the provided YouTube URL...")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([youtube_url])

audio_filename = "downloaded_audio.wav"

if os.path.exists(audio_filename):
    print("Loading OpenAI Whisper model (tiny) into memory...")
    model = whisper.load_model("tiny")

    print("Transcribing audio to text using Whisper...")
    result = model.transcribe(audio_filename)

    print("\n" + "=" * 50)
    print("YOUTUBE VIDEO TRANSCRIPTION RESULT:")
    print("=" * 50)
    print(result["text"])
    print("=" * 50)
    print("Pipeline execution completed successfully.")
else:
    print("Error: Audio file could not be downloaded.")