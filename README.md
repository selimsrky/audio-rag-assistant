# Audio RAG Assistant (Universal Speech-to-Text Pipeline)

A robust, containerized end-to-end Python pipeline designed to ingest audio from online streams (YouTube) or local audio files (WhatsApp voice notes, Discord voice recordings, MP3, WAV, OGG, M4A), preprocess signals via FFmpeg, and transcribe speech locally using OpenAI Whisper ASR. Built to demonstrate practical AI engineering, dynamic volume mounting, and containerization principles.

---

## Key Features

- **Universal Audio Ingestion:** Automatically distinguishes between remote web streams (YouTube URLs) and local audio files.
- **Cross-Platform Drag-and-Drop:** Built-in URI parser handles macOS and Linux terminal path quirks (decoding URL escapes such as `%20` and stripping `file://` prefixes).
- **High-Fidelity Audio Extraction:** Uses `yt-dlp` paired with `FFmpeg` to extract audio streams and convert them into standardized 16-bit linear PCM WAV buffers.
- **Local Neural ASR:** Runs OpenAI Whisper models (`tiny`) locally on CPU in FP32 precision with zero third-party cloud API dependencies.
- **Reproducible Containerization:** Packaged with Docker for dependency isolation and dynamic host filesystem mapping across macOS and Linux.

---

## Tech Stack

- **Python 3.10** (Containerized execution environment)
- **OpenAI Whisper** (Local neural speech recognition)
- **yt-dlp** (Media stream parsing and extraction)
- **FFmpeg** (Audio decoding, conversion, and post-processing)
- **Docker** (Container runtime and host volume virtualization)

---

## Repository Structure

```text
audio-rag-assistant/
├── Dockerfile           # Multi-stage container definitions and system packages
├── requirements.txt     # Locked Python dependencies (whisper, yt-dlp, etc.)
├── main.py              # Core application pipeline logic
├── run.sh               # Optional helper script for macOS / Linux
├── .gitignore           # Ignores OS artifacts (.DS_Store) and local files
└── README.md            # Technical documentation and setup guide
```

---

## Getting Started

### Prerequisites
Ensure you have Docker installed and running on your host system:
- **macOS:** Docker Desktop for Mac
- **Linux:** Docker Engine

### Step 1: Clone the Repository
```bash
git clone [https://github.com/selimsrky/audio-rag-assistant.git](https://github.com/selimsrky/audio-rag-assistant.git)
cd audio-rag-assistant
```

### Step 2: Build the Docker Image
Build the container image once. Subsequent runs will use the cached layer state:
```bash
docker build -t audio-rag-assistant .
```

### Step 3: Run the Pipeline
You can run the application directly via Docker or use the automated launcher script.

#### Option A: Direct Docker Command (macOS & Linux)
Mount the working directory and your user home directory (`$HOME`) so the container can access your Desktop and Downloads folders:
```bash
docker run --rm -it -v $(pwd):/app -v "$HOME:$HOME" audio-rag-assistant
```

#### Option B: Automated Helper Script (run.sh)
Create a single-command launcher (run once in terminal):
```bash
echo 'docker run --rm -it -v $(pwd):/app -v "$HOME:$HOME" audio-rag-assistant' > run.sh && chmod +x run.sh
```

Then launch whenever needed using:
```bash
./run.sh
```

---

## Usage Guide & Input Formats

Once launched, the pipeline prompts you for an input:
```text
Enter YouTube URL or drag & drop audio file:
```

### 1. YouTube Audio Ingestion
Paste any YouTube URL directly into the prompt:
```text
[https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
```
The pipeline automatically downloads the optimal audio track, converts it to a 192kbps WAV file, and passes it to the Whisper model.

### 2. Local Audio File Ingestion (WhatsApp, Discord, Voice Memos)
Drag and drop any local audio file directly into the terminal window, or specify its absolute/relative path:
- **WhatsApp Voice Notes:** `.ogg` / Opus format
- **Standard Audio:** `.mp3`, `.wav`, `.m4a`, `.flac`
- **Example input:** `/Users/username/Downloads/voice_note.ogg`

The pipeline cleans escaped path characters, verifies file existence, and outputs the transcribed text directly to standard output.

---

## Host Filesystem Mapping (macOS vs Linux)

| Parameter | Purpose | macOS Behavior | Linux Behavior |
| :--- | :--- | :--- | :--- |
| `-v \$(pwd):/app` | Live code sync | Maps repository to container `/app` | Maps repository to container `/app` |
| `-v "$HOME:$HOME"` | Desktop/Downloads access | Maps `/Users/<user>` into container | Maps `/home/<user>` into container |
