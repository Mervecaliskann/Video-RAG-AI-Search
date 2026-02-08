# 1. Python 3.10 tabanlı hafif bir Linux sürümü kullan
FROM python:3.10-slim

# 2. Çalışma klasörünü ayarla
WORKDIR /app

# 3. OpenCV için gerekli sistem kütüphanelerini yükle (İSİM DÜZELTİLDİ)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 4. Proje dosyalarını konteynerin içine kopyala
COPY . .

# 5. Python kütüphanelerini yükle
RUN pip install --no-cache-dir \
    streamlit \
    opencv-python-headless \
    pinecone-client \
    sentence-transformers \
    torch \
    Pillow \
    python-dotenv \
    "numpy<2.0" \
    "filelock<3.13"

# 6. Streamlit portunu dışarı aç
EXPOSE 8501

# 7. Uygulamayı başlat
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]