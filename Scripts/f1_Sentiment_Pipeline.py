from newsapi import NewsApiClient
import pandas as pd
from transformers import pipeline


newsapi = NewsApiClient(api_key='your_key_here') # Remplacez par votre clé API NewsAPI

# On cherche les articles qui mentionnent "Ferrari F1" ou "Leclerc"
data = newsapi.get_everything(q='Ferrari F1 OR Leclerc',
                                  language='en',
                                  sort_by='relevancy',
                                  page_size=100)

articles = data['articles']
df_news = pd.DataFrame(articles)

# le titre et la description pour l'IA
df_news = df_news[['publishedAt', 'title', 'description', 'source']]



# Initialisation du modèle

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# (Titre + Description) 

df_news['full_text'] = df_news['title'].fillna('') + " " + df_news['description'].fillna('')

#  Fonction pour analyser le sentiment (on limite à 512 caractères pour BERT)
def get_sentiment(text):
    if not text.strip(): return "NEUTRAL", 0.0
    # On tronque pour éviter les erreurs de longueur du modèle
    result = sentiment_pipeline(text[:512])[0]
    return result['label'], result['score']


print("Analyse du sentiment en cours...")
df_news[['label', 'score']] = df_news['full_text'].apply(lambda x: pd.Series(get_sentiment(x)))

# Transformation pour Power BI (Score positif/négatif)

df_news['final_score'] = df_news.apply(lambda x: x['score'] if x['label'] == 'POSITIVE' else -x['score'], axis=1)

print("Analyse terminée !")
df_news[['title', 'label', 'final_score']].head()

drivers = ['Leclerc', 'Sainz', 'Verstappen', 'Hamilton', 'Norris', 'Alonso']

#LIER LES NEWS AUX PILOTES POUR UNE MEILLEURE VISUALISATION DANS POWER BI

def tag_driver(text):
    for driver in drivers:
        if driver.lower() in text.lower():
            return driver
    return "General / Other"

df_news['Driver'] = df_news['full_text'].apply(tag_driver)

#EXPORTATION DE LA DATA

df_news.to_csv('f1_news_sentiment.csv', index=False)