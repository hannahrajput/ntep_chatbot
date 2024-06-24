import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from sklearn.pipeline import make_union, make_pipeline
from sklearn.preprocessing import Normalizer

# Load the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')


df = pd.read_csv('KBaseExtract 07Jun2024 - ContentPages.csv')
df = df.rename(columns={
    'LinkedNodeID': 'linked_node_id',
    'nid ( Content Page ID)': 'node_id',
    'Lang': 'lang',
    'title ( Content page title)': 'node_title',
    'H5Pcontent': 'h5p_content'
})

def preprocess_text(text):
    # Normalize text, remove special characters, and handle parentheses
    # text = text.lower()
    # text = re.sub(r'\([^)]*\)', '', text)  # remove parentheses and content within
    # text = re.sub(r'[^a-z0-9\s]', '', text)  # remove non-alphanumeric characters
    # return text.strip()
    text = text.lower()
    text = re.sub(r'\([^)]*\)', '', text)  # remove content within parentheses
    return text.strip()

df['processed_node_title'] = df['node_title'].apply(preprocess_text)

# Creating a hybrid vectorizer that includes word embeddings and tf-idf with char n-grams
class EmbeddingVectorizer:
    def __init__(self, model):
        self.model = model
        self.dim = model.get_sentence_embedding_dimension()

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return self.model.encode(X, convert_to_tensor=True, show_progress_bar=False).cpu().numpy()

tfidf_char_vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 4))
embedding_vectorizer = EmbeddingVectorizer(model)

vectorizer = make_pipeline(
    make_union(tfidf_char_vectorizer, embedding_vectorizer),
    Normalizer()
)

node_titles = df['processed_node_title'].tolist()
X = vectorizer.fit_transform(node_titles)


def find_node_ids(query):
    print(query)
    similarity_threshold = 0.4
    processed_query = preprocess_text(query)
    query_vector = vectorizer.transform([processed_query])

    cosine_similarities = cosine_similarity(query_vector, X).flatten()

    # Create a list of tuples (index, score) and filter based on the similarity threshold
    matched_scores = [(i, score) for i, score in enumerate(cosine_similarities) if score > similarity_threshold]

    # Sort the matched indices based on the scores in descending order to get highest scores first
    matched_scores_sorted = sorted(matched_scores, key=lambda x: x[1], reverse=True)

    # Extract unique node IDs from the sorted list, ensuring the highest score comes first
    unique_node_ids = []
    seen_node_ids = set()
    exact_match_index = None

    # Check for an exact match first and prioritize it
    for index, _ in matched_scores_sorted:
        node_title = df.iloc[index]['node_title']
        # print(query, node_title)
        if node_title.strip().lower() == query.strip().lower():
            exact_match_index = index
            break
    print(exact_match_index)
    # If an exact match is found, add it first
    if exact_match_index is not None:
        node_id = df.iloc[exact_match_index]['node_id']
        if node_id not in seen_node_ids:
            seen_node_ids.add(node_id)
            unique_node_ids.append(node_id)

    # Continue with other matches
    for index, _ in matched_scores_sorted:
        node_id = df.iloc[index]['node_id']
        if node_id not in seen_node_ids:
            seen_node_ids.add(node_id)
            unique_node_ids.append(node_id)

    # Generate URLs for the unique node IDs in order of descending similarity
    urls = [f"https://ntep.in/node/{node_id}" for node_id in unique_node_ids]
    # print(urls)
    return urls







