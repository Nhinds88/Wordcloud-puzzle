from PIL import Image
# from py_random_words import RandomWords
from randword import word
from quote import quote
from wordcloud import WordCloud, STOPWORDS
from bing_image_downloader import downloader
import numpy as np
import pytesseract
import os
import shutil

# r = RandomWords()
# w = r.get_word()
# print("Keyword Generated: ",w)
# https://randword.readthedocs.io/en/stable/usage.html
w = word(include_pos=['noun'])
print("Keyword Generated: ",w)
 
res = quote(w, limit=1)
for i in range(len(res)):
    txt = res[i]['quote']
    
downloader.download(w, limit=1,  output_dir='images', adult_filter_off=True, force_replace=False, timeout=60, filter='transparent', verbose=False)

# read the mask / color image taken from
alice_coloring = np.array(Image.open(os.path.join("images/"+w+"/Image_1.png")))
stopwords = set(STOPWORDS)
stopwords.add(w)

wc = WordCloud(background_color="black", prefer_horizontal= 1, max_words=200000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud
wc.generate(txt)

img = wc.to_image()
img.show()
img = img.save("temp.png")

# image text read
image_path = r"temp.png"
img2read = Image.open(image_path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(img2read)

print(text[:-1])

def handler(func, path, exc_info):
    print("Inside handler")
    print(exc_info)
    
path = 'images'
shutil.rmtree(path, onerror= handler)