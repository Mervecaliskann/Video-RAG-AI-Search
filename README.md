# 🎥 AI Video Search Engine (Multimodal RAG)

This project is a high-performance **AI Video Search Engine** that enables **semantic search** within video content. By leveraging Multimodal RAG (Retrieval-Augmented Generation), it allows users to find specific moments in a video using natural language queries like "a dog walking" or "scenic sunset".



## 🚀 Key Features

* **Multimodal Semantic Search:** Bridges the gap between text and video using the **CLIP (Contrastive Language-Image Pre-training)** model to map different data types into the same vector space.
* **Frame-Level Analysis:** Uses **OpenCV** to intelligently extract keyframes from videos at precise intervals for processing.
* **Vector Database Power:** Employs **Pinecone** for ultra-fast similarity searches across thousands of stored video embeddings.
* **Multilingual Support:** Capable of understanding both English and Turkish queries (e.g., searching for both "dog" and "köpek").
* **Flexible Format Support:** Fully compatible with `.mp4` and `.mov` video formats.
* **Modern UI:** A clean, responsive dashboard built with **Streamlit** for seamless video uploads and real-time visual results.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.10 |
| **AI Models** | `sentence-transformers/clip-ViT-B-32` |
| **Vector Database** | Pinecone |
| **Backend Libraries** | OpenCV, PyTorch, Pillow, python-dotenv |
| **Frontend** | Streamlit |
| **Deployment** | Docker (Configuration ready for containerization) |

---

## 🏗️ How it Works

1.  **Frame Extraction:** When a video is uploaded, **OpenCV** breaks the video into individual frames to represent the timeline.
2.  **Vectorization (Embedding):** Each frame is passed through the CLIP model, converting visual pixels into a **512-dimensional numerical vector**.
3.  **Indexing:** These vectors are stored in **Pinecone** along with their specific timestamps.
4.  **Semantic Retrieval:** The user's text query is vectorized and compared against the stored frames using **Cosine Similarity**:
    $$similarity = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$
    The system then returns the moments in the video that best match the query.

---

## 📦 Local Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/Mervecaliskann/Video-RAG-AI-Search.git](https://github.com/Mervecaliskann/Video-RAG-AI-Search.git)
cd Video-RAG-AI-Search
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Setup

Create a .env file in the root directory and add your Pinecone credentials:
```bash
PINECONE_API_KEY=your_pinecone_key
INDEX_NAME=video-search
```
### 4. Run the Application
```bash
streamlit run app.py
```

### 🐳 Deployment Note (Docker)
This repository includes a Dockerfile designed for professional containerized deployment. While the project is currently optimized for local execution, the Docker configuration serves as a blueprint for scaling the application to cloud environments.

### 📂 Project Structure

*  app.py: Main Streamlit interface and application logic.

*  modules/processor.py: Handles video-to-frame conversion logic.

*  modules/embedder.py: Manages CLIP model loading and embedding generation.

*  modules/vector_db.py: Interface for Pinecone storage and similarity search.

*  requirements.txt: List of all necessary Python libraries.


### 👤 Author

Merve Caliskan

M.Sc. in Data Science Student
