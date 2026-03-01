# SeaDoc Secure Processor

A production-ready document conversion system designed with a focus on privacy, security, and containerized microservices. This project demonstrates a full-stack implementation using modern tools to handle sensitive document processing in an isolated environment.

---

## Technical Architecture

The application is architected into three decoupled layers to ensure scalability and security:

| Component | Technology | Role |
| --- | --- | --- |
| **Frontend** | Vue.js 3 / Vite | Responsive UI & Binary Stream Handling |
| **Backend** | FastAPI / Python 3.10 | Business Logic & PDF Generation |
| **Proxy** | Nginx Proxy Manager | SSL (HTTPS) Termination & Reverse Proxy |
| **Infrastructure** | Docker / Compose | Container Orchestration & Networking |

---

## Core Features & Highlights

* **Isolated Conversions:** Leveraging **LibreOffice Headless** and **img2pdf** inside Linux containers to ensure complex document rendering without a GUI.
* **Secure Networking:** Implemented a **Reverse Proxy** with **Nginx Proxy Manager**, managing encrypted traffic (SSL/TLS) via Let's Encrypt.
* **Privacy-First:** Files are processed in ephemeral `/tmp` storage. No data is stored permanently; documents are streamed directly to the user as binary blobs.
* **Modern Frontend:** Built with **Tailwind CSS** for a clean, professional UI, and **Vite** for optimized build performance.

---

## Project Structure

```text
seadoc/
├── backend/            # FastAPI application, LibreOffice & Dockerfile
├── frontend/           # Vue.js source code, Tailwind config & Vite
├── nginx/              # Proxy data & SSL certificate volumes
└── docker-compose.yml  # Main orchestration for microservices

```

---

## Installation and Deployment

### Prerequisites

* Docker and Docker Compose installed.
* Ports 80, 81, and 443 open on your host/firewall.

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/vmC0sta/seadoc-secure-processor.git
cd seadoc-secure-processor

```


2. **Deploy the stack:**
```bash
docker-compose up -d --build

```


3. **Configure the Domain:**
Access the Nginx Admin Panel at `http://your-ip:81` to map your domain (e.g., `seadoc.duckdns.org`) to the frontend service on port `5173`.

---

## Technical Implementation Details

### API Design

The backend uses **FastAPI** for its high performance and native support for asynchronous requests. Document conversion is handled via system-level subprocess calls, ensuring that Word (`.docx`) and Excel (`.xlsx`) files maintain 1:1 formatting accuracy when exported to PDF.

### Frontend Data Handling

Instead of simple links, the frontend utilizes the **Fetch API** to process binary responses. It generates a temporary `blob` URL to trigger an immediate, secure download of the generated PDF without exposing internal server paths.

### Security

SSL certificates are managed automatically. By using a dedicated Nginx container, the application is shielded from direct external access, exposing only the strictly necessary ports.

---

*Developed by vmC0sta - 2026.*
