from sklearn.metrics.pairwise import cosine_similarity

def search_similar(query_embedding, chunk_embeddings, chunks, top_k=3):
    similarities = cosine_similarity([query_embedding], chunk_embeddings)[0]

    ranked = sorted(
        zip(chunks, similarities),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]