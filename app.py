import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the cleaned data
df = pd.read_csv('cleaned_assessments.csv')

# Create a TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Function to get recommendations
def get_recommendations(query, top_n=10):
    query_tfidf = tfidf.transform([query])
    cosine_similarities = linear_kernel(query_tfidf, tfidf_matrix).flatten()
    related_docs_indices = cosine_similarities.argsort()[:-top_n-1:-1]
    return df.iloc[related_docs_indices]

# Streamlit app
st.title("SHL Assessment Recommendation System")
query = st.text_input("Enter job description or query:")
if query:
    recommendations = get_recommendations(query)
    st.write(recommendations[['name', 'link', 'remote_testing', 'adaptive_irt', 'test_type']])