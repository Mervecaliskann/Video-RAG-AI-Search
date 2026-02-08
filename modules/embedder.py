#(CLIP Modeli - Beyin) Bu kod, resimleri ve metinleri vektöre çevirir.
from sentence_transformers import SentenceTransformer
from PIL import Image

class ClipEmbedder:
    def __init__(self):
        # CLIP modelini indiriyoruz (Hafif ve hızlı versiyon)
        print("Model yükleniyor...")
        self.model = SentenceTransformer('clip-ViT-B-32')

    def get_image_embedding(self, image_path):
        img = Image.open(image_path)
        return self.model.encode(img).tolist()

    def get_text_embedding(self, text):
        return self.model.encode(text).tolist()