# Audio RAG Assistant (YouTube to Text Pipeline)

A robust, containerized end-to-end Python pipeline that extracts audio

## Tech Stack
- **Python 3.10** (Isolated inside Docker)
- **OpenAI Whisper** (Local ASR model execution in FP32)
- **yt-dlp** (Advanced YouTube audio stream extraction)
- **FFmpeg** (Audio post-processing and WAV conversion)

## Getting Started (Docker Installation)

1. Clone the repository:
```bash
git clone https://github.com/selimsrky/audio-rag-assistant.git
cd audio-rag-assistant
```

2. Build the Docker image:
```bash
docker build -t audio-rag-assistant .
```

3. Run the container interactively:
```bash
docker run --rm -it audio-rag-assistant
```

4. Paste any YouTube video URL when prompted to get the complete transcription directly in your terminal.
```bash
https://www.youtube.com/watch?v=dQw4w9WgXcQ  # Example YouTube URL
```