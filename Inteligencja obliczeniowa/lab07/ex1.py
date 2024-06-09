import matplotlib
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from wordcloud import WordCloud

matplotlib.use("QtAgg")

nltk.download(["punkt", "stopwords", "wordnet", "vader_lexicon"])

with open("article.txt", "r") as fh:
    article = fh.read()

article = article.strip().replace("\n", "").strip()

tokens = nltk.word_tokenize(article)

# print(nltk.FreqDist(tokens).most_common(10))
print(f"Count with stop words: {len(nltk.FreqDist(tokens))}")

# delete stopwords
stop_words = set(stopwords.words("english"))
tokens = [tok for tok in tokens if tok not in stop_words]
# print(nltk.FreqDist(tokens).most_common(10))
print(f"Count without stop words: {len(nltk.FreqDist(tokens))}")

# lemmatization
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(tok) for tok in tokens]
print(f"Count after lemmatization: {len(nltk.FreqDist(tokens))}")

# plot of the most common words
plt.figure(figsize=(10, 5))
nltk.FreqDist(tokens).plot(10)
plt.show()

wordcloud = WordCloud(max_font_size=40).generate(" ".join(tokens))
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
