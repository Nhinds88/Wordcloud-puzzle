from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pytesseract

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'words.txt')).read()

# read the mask / color image taken from
# http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
alice_coloring = np.array(Image.open(path.join(d, "goron.png")))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="black", prefer_horizontal= 1, max_words=200000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud
wc.generate(text)

img = wc.to_image()
# img.show()
img = img.save("temp.png")



# image text read
image_path = r"temp.png"
img2read = Image.open(image_path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(img2read)

print(text[:-1])

# imgSRC = cv2.imread("temp.png")
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# gray = cv2.cvtColor(imgSRC, cv2.COLOR_BGR2GRAY)

# ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))

# dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# contours, hierchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# im2 = imgSRC.copy()

# # A text file is created and flushed
# file = open("recognized.txt", "w+")
# file.write("")
# file.close()

# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
     
#     # Drawing a rectangle on copied image
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
#     # Cropping the text block for giving input to OCR
#     cropped = im2[y:y + h, x:x + w]
     
#     # Open the file in append mode
#     file = open("recognized.txt", "a")
     
#     # Apply OCR on the cropped image
#     text = pytesseract.image_to_string(cropped)
     
#     # Appending the text into file
#     file.write(text)
#     file.write("\n")
     
#     # Close the file
#     file.close

# # create coloring from image
# image_colors = ImageColorGenerator(alice_coloring)

# show
# fig, axes = plt.subplots(1, 3)
# axes[0].imshow(wc, interpolation="bilinear")
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
# axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
# axes[2].imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
# for ax in axes:
#     ax.set_axis_off()
# plt.show()