# Usa uma imagem leve do Python
FROM python:3.10-slim

# Instala o LibreOffice e dependências de sistema
RUN apt-get update && apt-get install -y \
    libreoffice \
    ffmpeg \
    libmagic1 \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o requirements e instala as bibliotecas Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do códig
COPY . .

# Comando para subir a API com recarregamento automático
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]