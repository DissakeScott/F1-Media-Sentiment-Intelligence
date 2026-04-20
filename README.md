# 🏎️ F1 Media Intelligence Dashboard
**Sentiment Analysis of Formula 1 News using DistilBERT & Power BI**

## 📌 Project Overview
This project is an end-to-end Data & AI pipeline designed to track the "media reputation" of F1 drivers. It automates the collection of international news and uses Deep Learning to quantify the sentiment around each driver.

## 🛠️ Tech Stack
* **Data Ingestion:** NewsAPI (Python)
* **AI/NLP:** Hugging Face `Transformers` (DistilBERT base uncased)
* **Data Processing:** Pandas / NumPy
* **Visualization:** Power BI Desktop (DAX, Star Schema, Key Influencers)
* **Environment:** Ubuntu 24.04 (Noble Numbat)

## 📊 Key Features
1. **Automated Scraping:** Fetches 100+ latest articles per driver.
2. **Sentiment Scoring:** Uses a fine-tuned DistilBERT model to score text from -1 (Negative) to +1 (Positive).
3. **Interactive Dashboard:** - **Time-series Analysis:** Track how sentiment evolves after a race.
    - **Share of Voice:** Compare media coverage volume between drivers.
    - **Driver Performance vs Media:** Correlation between results and press tone.

## 🚀 How to Run
1. Get your API key from [newsapi.org](https://newsapi.org).
2. Run the script `notebooks/f1_scraper_ai.py`.
3. Import the generated CSV into Power BI.

<img width="771" height="439" alt="Capture d’écran du 2026-04-20 08-35-57" src="https://github.com/user-attachments/assets/b24d42be-0576-4841-aa84-6ebaa674d6eb" />

