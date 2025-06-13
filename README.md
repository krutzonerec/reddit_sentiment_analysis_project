# Reddit Duygu Analizi Projesi

Bu proje, belirli bir subreddit'teki gönderileri çekerek başlıkları üzerinde duygu analizi yapan ve sonuçları görselleştiren bir Python uygulamasıdır.

---

## Özellikler

- Reddit API kullanarak gönderi verisi toplar.
- Başlıklar üzerinde duygu analizi yapar (Pozitif, Negatif, Nötr).
- Duygu dağılımını pasta grafiği olarak görselleştirir.
- Sonuçları CSV dosyasına kaydeder.

---

## Proje Yapısı

```
proje_kök_klasörü/
│
├── main.py
├── data/
│   └── reddit_posts.csv              # Çekilen verilerin kaydedildiği dosya
│
├── config/
│   └── config.py                     # Reddit API kimlik bilgileri
│
├── src/
│   ├── reddit_scraper.py            # Reddit'ten veri çeken modül
│   ├── sentiment_analyzer.py        # Duygu analizi yapan modül
│   └── visualizer.py                # Veriyi görselleştiren modül
```

---

##  Kurulum

### 1. Gerekli Kütüphaneler

```bash
pip install praw pandas textblob matplotlib
python -m textblob.download_corpora
```

### 2. `config/config.py` Dosyasını Oluştur

```python
# config/config.py

import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="sentiment-analysis-script by u/YOUR_USERNAME"
)
```

 Not: Reddit API bilgilerini almak için [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) adresinden bir uygulama oluşturmalısınız.

---

##  Kullanım

```bash
python main.py
```

Bu komut:
- Reddit'ten gönderileri çeker.
- Başlıklar üzerinde duygu analizi yapar.
- Sonuçları `data/reddit_posts.csv` dosyasına kaydeder.
- Duygu dağılımını grafik olarak gösterir.

---

## Örnek Çıktı

Pasta grafik: Pozitif / Negatif / Nötr başlık oranlarını gösterir.

---

## 📌 Notlar

- Varsayılan subreddit: `r/turkey`
- Varsayılan arama kelimesi: `"deprem"`
- Maksimum gönderi: `1500`
- Bunları `fetch_posts()` fonksiyonu parametreleri ile özelleştirebilirsiniz.

---

##  Lisans

MIT Lisansı
