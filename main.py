from wordcloud import WordCloud, STOPWORDS
import wikipedia
from PIL import Image

# https://www.youtube.com/watch?v=o7NFZ78CH-0

stopword = set(STOPWORDS)
info = wikipedia.summary("Python")
word_cloud = WordCloud(stopwords = stopword).generate(info)
img = word_cloud.to_image()
img.show()