from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_job_description(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def match_resume_to_jd(resume_text, jd_text):
    texts = [resume_text, jd_text]
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(texts)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return similarity * 100  # Convert to percentage
