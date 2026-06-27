from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def ats_score(resume, jd):
    tfidf = TfidfVectorizer().fit_transform([resume, jd])
    score = cosine_similarity(tfidf[0], tfidf[1])[0][0]
    return round(score * 100, 2)