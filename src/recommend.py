import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('imdb_top_1000.csv')
print(df.head())

content = (df['Series_Title'].str.cat(df[['Overview', 'Director', 'Genre']], sep=' ')).tolist()
recom_df = pd.DataFrame(content, columns=['Content'], index=df['Series_Title'])

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(recom_df['Content'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
cos_df = pd.DataFrame(cosine_sim, columns=df['Series_Title'])
cos_df['Series_Title'] = df['Series_Title']
cos_df = cos_df[['Series_Title'] + cos_df.columns[:-1].to_list()]

idxs = pd.Series(df.index, index=df['Series_Title'])

def get_recommendations(title):
    idx = idxs[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[:11]

    movie_indices = [i[0] for i in sim_scores]

    if 'Stars' in df.columns:
        columns_to_select = ['Series_Title', 'Released_Year', 'Genre', 'Runtime', 'Overview', 'Stars', 'Director', 'IMDB_Rating', 'Meta_score', 'Gross']
    else:
        columns_to_select = ['Series_Title', 'Released_Year', 'Genre', 'Runtime', 'Overview', 'Star1', 'Star2', 'Star3', 'Star4', 'Director', 'IMDB_Rating', 'Meta_score', 'Gross']

    recommendations = df.iloc[movie_indices][columns_to_select]

    return recommendations

movie_title = "Inception"
recommendations = get_recommendations(movie_title)
print(f"Recommended movies for '{movie_title}':")
print(recommendations)
