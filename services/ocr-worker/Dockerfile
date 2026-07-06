FROM python:3.12-slim
WORKDIR /app

# Install system dependencies required for OpenCV and PaddleOCR
# Note: libgl1-mesa-glx is replaced by libgl1 in newer Debian versions
RUN apt-get update && apt-get install -y     libgl1     libglib2.0-0     libsm6     libxext6     libxrender-dev     libgomp1     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["celery", "-A", "app.core.celery_app", "worker", "--loglevel=info", "--queues=ocr_queue"]
