def clean_text(text):
    text = " ".join(text.split())
    return text

def chunk_text(text, chunk_size=500, overlap=100):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

def process_documents(documents):
    all_chunks = []

    for doc in documents:
        cleaned = clean_text(doc["text"])
        chunks = chunk_text(cleaned)

        for chunk in chunks:
            all_chunks.append({
                "url": doc["url"],
                "text": chunk
            })

    return all_chunks