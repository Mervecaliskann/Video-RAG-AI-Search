#(Pinecone - Hafıza) Verileri buluta kaydeder ve arama yapar.
import os
import time
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

class VectorDB:
    def __init__(self, index_name="video-rag"):
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index_name = index_name
        
        # İndeks yoksa oluştur
        existing_indexes = [i.name for i in self.pc.list_indexes()]
        if index_name not in existing_indexes:
            self.pc.create_index(
                name=index_name,
                dimension=512, # CLIP çıktısı 512 boyuttur
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )
            time.sleep(1)

        self.index = self.pc.Index(index_name)

    def upsert_vectors(self, vectors):
        # vectors: [(id, embedding, metadata), ...]
        self.index.upsert(vectors=vectors)

    def search(self, query_vector, top_k=3):
        return self.index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True
        )