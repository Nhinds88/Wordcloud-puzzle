# # from random_word import RandomWords
# # from quote import quote

# # r = RandomWords()
# # w = r.get_random_word()
# # print("Single Random Word: "+w)

# # res = quote('family', limit=4)
# # print(res)

# from random_word import RandomWords
# from quote import quote
 
# r = RandomWords()
# w = r.get_random_word()
# print("Keyword Generated: ",w)
 
# res = quote(w, limit=1)
# for i in range(len(res)):
#     # print(i)
#     txt = res[i]['quote']
# print(txt)
# # print(res)

# from google_images_download import google_images_download   #importing the library

# response = google_images_download.googleimagesdownload()   #class instantiation

# arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
# paths = response.download(arguments)   #passing the arguments to the function
# print(paths)   #printing absolute paths of the downloaded images
from bing_image_downloader import downloader
downloader.download('dog', limit=1,  output_dir='images', adult_filter_off=True, force_replace=False, timeout=60, filter='transparent', verbose=True)
