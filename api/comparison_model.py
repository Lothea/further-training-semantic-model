from sentence_transformers import SentenceTransformer, util
from collections import OrderedDict


model = SentenceTransformer('all-MiniLM-L6-v2')

def similarity(sentences1, sentences2):

    embeddings1 = model.encode(sentences1, convert_to_tensor=True)
    embeddings2 = model.encode(sentences2, convert_to_tensor=True)

    cosine_scores = util.cos_sim(embeddings1, embeddings2)
    result = []

    similarities = OrderedDict()
    for i, sentence in enumerate(sentences1):
        cosine_scores = util.cos_sim(embeddings1[i : i + 1], embeddings2)[0]
        top_3 = sorted(
            range(len(cosine_scores)), key=lambda j: cosine_scores[j], reverse=True
        )[:5]
        similarities[sentence] = [(sentences2[j], cosine_scores[j]) for j in top_3]


    result = [
        [sentence, questions, round(score.item(),2)]
        for sentence, pairs in similarities.items()
        for questions, score in pairs
    ]
    
    return result
