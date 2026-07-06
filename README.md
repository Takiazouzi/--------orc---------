# 📄 Smart Document AI

An intelligent AI-powered document processing platform that extracts handwritten English and French documents, understands their semantic meaning, and automatically organizes them into categories.

---

## 🚀 Features

- 📝 Handwritten OCR (English & French)
- 🖼️ Image preprocessing for enhanced OCR accuracy
- 🌍 Automatic language detection
- 🧹 Text cleaning and normalization
- 🧠 Semantic embeddings using Transformer models
- 📂 Automatic document categorization
- ➕ Dynamic category creation for new document types
- 🔍 Semantic document search
- 📊 Confidence scoring
- 📦 REST API with FastAPI
- 🐳 Docker support
- ✅ Unit & Integration testing

---

## 🏗️ System Architecture

```text
                    Document Upload
                           │
                           ▼
                Image Preprocessing
                           │
                           ▼
                     OCR Extraction
                           │
                           ▼
                  Language Detection
                           │
                           ▼
                    Text Cleaning
                           │
                           ▼
                Embedding Generation
                           │
                           ▼
              Category Decision Engine
               ┌────────────┴────────────┐
               ▼                         ▼
     Existing Category          Create New Category
               │                         │
               └────────────┬────────────┘
                            ▼
                PostgreSQL + pgvector
                            │
                            ▼
                   REST API / Dashboard
```

---

## 📁 Project Structure

```text
smart-document-ai/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── pipeline/
│   │   └── stages/
│   ├── services/
│   ├── repositories/
│   ├── database/
│   ├── models/
│   ├── utils/
│   └── main.py
│
├── data/
├── models/
├── tests/
├── docker/
├── scripts/
├── notebooks/
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 🔄 Processing Pipeline

```text
Image
  │
  ▼
Image Preprocessing
  │
  ▼
OCR Extraction
  │
  ▼
Language Detection
  │
  ▼
Text Cleaning
  │
  ▼
Embedding Generation
  │
  ▼
Semantic Similarity Search
  │
  ▼
Category Assignment / Creation
  │
  ▼
Database Storage
```

---

## 🧠 AI Components

### OCR
- PaddleOCR
- TrOCR (Future Enhancement)

### Image Processing
- OpenCV
- Adaptive Thresholding
- Deskew
- Noise Removal
- Contrast Enhancement

### NLP
- Sentence Transformers
- Language Detection
- Text Normalization

### Classification
- Cosine Similarity
- Automatic Category Creation
- Semantic Search

---

## 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Language | Python 3.12 |
| API | FastAPI |
| OCR | PaddleOCR |
| Image Processing | OpenCV |
| NLP | Sentence Transformers |
| Language Detection | Lingua |
| Database | PostgreSQL |
| Vector Search | pgvector |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Testing | Pytest |
| Deployment | Docker |

---

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/smart-document-ai.git

cd smart-document-ai

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## 📚 Development Roadmap

- [x] Project initialization
- [ ] FastAPI Backend
- [ ] Image preprocessing
- [ ] PaddleOCR integration
- [ ] Language detection
- [ ] Text normalization
- [ ] Embedding generation
- [ ] Similarity engine
- [ ] Automatic category creation
- [ ] PostgreSQL integration
- [ ] Semantic search
- [ ] REST API endpoints
- [ ] Dashboard
- [ ] Docker deployment
- [ ] CI/CD Pipeline

---

## 🎯 Future Improvements

- Multi-page PDF support
- Batch processing
- GPU acceleration
- Fine-tuned OCR models
- User authentication
- Human review workflow
- Elasticsearch integration
- Export to PDF / JSON / CSV
- Document versioning
- Real-time processing

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Built as an end-to-end AI Engineering project demonstrating OCR, Computer Vision, Natural Language Processing, Semantic Search, Vector Databases, and Intelligent Document Understanding.

