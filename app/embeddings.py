from sentence_transformers import SentenceTransformer

model = None

def get_model():
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model

def generate_embeddings(texts):
    current_model = get_model()
    return current_model.encode(texts, convert_to_numpy=True)