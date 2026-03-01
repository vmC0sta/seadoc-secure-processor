SeaDoc Secure Processor
A document processing and conversion system focused on privacy and security. The application allows for isolated conversion of Word, Excel, and Image files to PDF format using Docker containers.

System Architecture
The project is divided into three main layers:

Frontend (Vue.js 3 + Vite + Tailwind CSS): A responsive user interface that manages file uploads and handles binary blobs for automatic browser downloads.

Backend (FastAPI + Python): An API that processes conversions using libraries such as img2pdf for images and the LibreOffice headless engine for office documents.

Proxy (Nginx Proxy Manager): Manages external traffic, port forwarding, and SSL encryption (HTTPS).

Conversion Features
Word to PDF: Supports .doc and .docx files via lowriter.

Excel to PDF: Supports .xls, .xlsx, and .ods files via libreoffice.

JPG to PDF: Direct conversion of .jpg, .jpeg, and .png images while preserving original quality.

System Requirements
Docker and Docker Compose installed.

Network connectivity on ports 80, 81 (admin panel), and 443.

Installation and Setup
Clone the repository:

Bash
git clone https://github.com/vmC0sta/seadoc-secure-processor.git
cd seadoc-secure-processor
Deploy the services via Docker Compose:

Bash
docker-compose up -d --build
Configure the Proxy Host in Nginx Proxy Manager (Port 81):

Domain Name: seadoc.duckdns.org (or your custom domain).

Forward Host/IP: 172.17.0.1 (Docker Gateway IP).

Forward Port: 5173.

Technical Implementation Details
Backend (Python/FastAPI)
The backend utilizes subprocesses to invoke system-level command-line tools (LibreOffice), ensuring that complex documents maintain their original formatting during conversion. Temporary files are processed within the container's /tmp directory, ensuring data isolation.

Frontend (Vue.js)
The application uses the Fetch API for asynchronous communication with the backend. Download processing is handled via window.URL.createObjectURL, allowing the browser to treat the binary data stream (PDF) as a physical file download immediately after conversion.

Security and Privacy
Processing occurs within ephemeral containers. Unlike public online converters, documents processed in SeaDoc are not stored permanently; they are discarded immediately after the response stream is generated for the client.
