from PIL import Image
from py_random_words import RandomWords
from randword import word
from quote import quote
from wordcloud import WordCloud, ImageColorGenerator
from bing_image_downloader import downloader
import numpy as np
import random
import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude

w = 'wordcloud'

txt = 'Take this kiss upon the brow! And, in parting from you now, Thus much let me avow You are not wrong, who deem That my days have been a dream; Yet if hope has flown away In a night, or in a day, In a vision, or in none, Is it therefore the less gone? All that we see or seem Is but a dream within a dream. I stand amid the roar Of a surf-tormented shore, And I hold within my hand Grains of the golden sand How few! yet how they creep Through my fingers to the deep, While I weep while I weep! O God! can I not grasp Them with a tighter clasp? O God! can I not save One from the pitiless wave? Is all that we see or seem But a dream within a dream?'

# read the mask / color image taken from
image_coloring = np.array(Image.open(os.path.join("cloud.webp")))
image_coloring = image_coloring[::3, ::3]
image_mask = image_coloring.copy()
image_mask[image_mask.sum(axis=2) ==0] = 255

edges = np.mean([gaussian_gradient_magnitude(image_coloring[:, :, i] / 255., 2) for i in range(3)], axis=0)
image_mask[edges > 0.08] = 255

stopwords = set(w)

wc = WordCloud(background_color="black", width=1000, height=800, prefer_horizontal= 1, max_words=200000, mask=image_mask,
            stopwords=stopwords, max_font_size=20, random_state=0, scale=10)
# generate word cloud
wc.generate(txt)

image_colors = ImageColorGenerator(image_coloring)
wc.recolor(color_func=image_colors)

img = wc.to_image()
img.show()
img = img.save("temp.png")