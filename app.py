#(Streamlit - Arayüz) Her şeyi birleştiren ana dosya.
import streamlit as st
import tempfile
import os
from modules.embedder import ClipEmbedder
from modules.vector_db import VectorDB
from modules.processor import VideoProcessor

st.set_page_config(page_title="Video RAG AI", layout="wide")
st.title("🎥 AI Video Search Engine")
st.write("Videoyu yükle, içindeki anı yazarak bul!")

# Modelleri yükle (Cache ile hızlandır)
@st.cache_resource
def load_models():
    return ClipEmbedder(), VectorDB()

embedder, vector_db = load_models()
processor = VideoProcessor()

# --- SOL TARAF: Yükleme ---
with st.sidebar:
    st.header("1. Video Yükle")
    uploaded_file = st.file_uploader("Video Seç", type=["mp4", "mov"])
    
    if uploaded_file and st.button("Videoyu İşle"):
        with st.spinner("Video karelere bölünüyor ve analiz ediliyor..."):
            # Geçici dosyaya kaydet
            tfile = tempfile.NamedTemporaryFile(delete=False) 
            tfile.write(uploaded_file.read())
            
            # Kareleri ayır
            frames = processor.process_video(tfile.name, interval=2)
            st.info(f"{len(frames)} kare çıkarıldı. Vektörleştiriliyor...")
            
            # Pinecone'a yükle
            vectors = []
            for f in frames:
                embedding = embedder.get_image_embedding(f["path"])
                metadata = {"path": f["path"], "timestamp": f["timestamp"]}
                vectors.append((f["id"], embedding, metadata))
            
            vector_db.upsert_vectors(vectors)
            st.success("✅ Video hafızaya alındı! Arama yapabilirsin.")

# --- SAĞ TARAF: Arama ---
query = st.text_input("Ne arıyorsun? (Örn: Kırmızı araba, ağlayan bebek)")

if query:
    # 1. Metni vektöre çevir
    query_vector = embedder.get_text_embedding(query)
    
    # 2. Pinecone'da ara
    results = vector_db.search(query_vector, top_k=3)
    
    # 3. Sonuçları göster
    st.subheader("Bulunan Sahneler:")
    cols = st.columns(3)
    for idx, match in enumerate(results['matches']):
        meta = match['metadata']
        score = match['score']
        
        with cols[idx]:
            # Resmi göster
            if os.path.exists(meta['path']):
                st.image(meta['path'])
                st.caption(f"⏱️ Saniye: {meta['timestamp']} | Güven: %{int(score*100)}")
            else:
                st.warning("Resim bulunamadı (Geçici dosya silinmiş olabilir)")