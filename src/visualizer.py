import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(df):
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="sentiment", palette="pastel")
    plt.title("Reddit Gönderilerinde Duygu Dağılımı")
    plt.xlabel("Duygu")
    plt.ylabel("Gönderi Sayısı")
    plt.tight_layout()
    plt.savefig("data/sentiment_distribution.png")
    plt.show()
