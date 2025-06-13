from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Pozitif"
    elif polarity < 0:
        return "Negatif"
    else:
        return "Nötr"
