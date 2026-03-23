from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import os
import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except:
        return ""


def preprocess_text(text):

    doc = nlp(text)

    clean_tokens = []

    for token in doc:
        if token.is_stop == False and token.is_punct == False:
            clean_tokens.append(token.lemma_.lower())

    return " ".join(clean_tokens)

def calculate_similarity(job_desc, resume_text):

    documents = [job_desc, resume_text]

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(documents)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return similarity_score[0][0]


def rank_resumes(job_description, resume_folder):

    results = []

    cleaned_job = preprocess_text(job_description)

    for file in os.listdir(resume_folder):

        if file.endswith(".pdf"):

            path = os.path.join(resume_folder, file)

            text = extract_text_from_pdf(path)

            cleaned_resume = preprocess_text(text)

            score = calculate_similarity(cleaned_job, cleaned_resume)

            results.append((file, score))

    results.sort(key=lambda x: x[1], reverse=True)

    return results


if __name__ == "__main__":

    job_description = """
    Looking for Python Developer with skills in
    Machine Learning, NLP, Flask and Data Science
    """

    rankings = rank_resumes(job_description, "resumes")

    print("\n===== RESUME RANKING =====\n")

    for rank, (file, score) in enumerate(rankings, start=1):
        print(f"{rank}. {file} ---> {score:.2f}")