# Reddit Sentiment Analysis

## Amaç
Reddit üzerinden belirli bir konuda (örneğin “deprem”) toplanan gönderilerin duygu analizini gerçekleştirmek.

## Kullanılan Kütüphaneler
- `praw` – Reddit API ile veri çekmek için
- `pandas` – Verileri işlemek için
- `textblob` – Sentiment analizi için
- `matplotlib` & `seaborn` – Grafik oluşturmak için

## Proje Yapısı
reddit_sentiment_analysis_project/
├── main.py
├── config/
│ └── config.py
├── src/
│ ├── reddit_scraper.py
│ ├── sentiment_analyzer.py
│ └── visualizer.py
├── data/
├── requirements.txt

bash
Kopyala
Düzenle

## Kurulum ve Çalıştırma

```bash
git clone ...
cd reddit_sentiment_analysis_project
pip install -r requirements.txt
python -m textblob.download_corpora
python main.py
