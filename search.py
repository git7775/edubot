#EduBot search Engine
#This finds the best answer from knowledge base

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from knowledge_base import knowledge

def find_answer(question):
    # Combine the question with the knowledge base
    all_text = knowledge + [question.lower()]

    # Convert text to numbers using TF-IDF vectors for the all_text
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_text)

    # Find which sentence is most similar to the question
    question_vector = tfidf_matrix[-1]  # The last vector is the question
    knowledge_vectors = tfidf_matrix[:-1]  # All vectors except the last one are from the knowledge base

    similarities = cosine_similarity(question_vector, knowledge_vectors).flatten()  # Calculate cosine similarity and flatten the result
    best_score = similarities.max()  # Get the similarity score of the most similar sentence
    if best_score < 0.1:
        return "I'm still learning. Can you ask another question?"
    
    best_match_index = similarities.argmax()  # Get the index of the most similar sentence
    # Return the most similar answer from the knowledge base
    return knowledge[best_match_index]