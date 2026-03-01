# SeaDoc
> A private, offline-first document processor and transcriber for sensitive data.

## The Privacy Challenge
Built to solve the security risks of uploading confidential government documents to public online converters. SeaDoc ensures that 100% of the processing happens locally on the user's machine. **No data ever leaves the local network.**

## Tech Stack
* **Frontend:** Vue.js 3 + Tailwind CSS (Clean, minimalist UI).
* **Backend:** Python (FastAPI) - high performance for file handling.
* **AI Engine:** OpenAI Whisper (running locally for Speech-to-Text).
* **PDF Engine:** PyMuPDF / Pikepdf.
* **Environment:** Docker & WSL2.

## Key Features
* **Secure PDF Tools:** Merge, split, and compress PDFs locally.
* **Local Transcription:** Transcribe audio/video to text using AI without internet access.
* **Image-to-PDF:** Batch convert scanned documents into a single searchable PDF.
* **Metadata Stripper:** Remove hidden sensitive metadata from office files.

## Architecture


## Local Setup (WSL2 / Docker)
1. Clone the repository.
2. Build the containers: `docker-compose up --build`.
3. Open `localhost:3000` to start processing files securely.

---
*Developed to provide a secure alternative for public servants handling confidential information.*
