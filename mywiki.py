import sys
from os import path
import os
import numpy as np
from PIL import Image
import wikipedia
import random
import secrets
from wordcloud import WordCloud, STOPWORDS


# get path to script's directory
currdir = path.dirname(__file__)

def get_result(query):
	# get best matching title for given query
	title = wikipedia.search(query)[0]

	# get wikipedia page for selected title
	page = wikipedia.page(title)
	return page.content

def create_wordcloud(text):
	imgs = ["apple.jpeg", "bfly.jpeg", "cloud.png", "monitor.jpeg", "star.jpeg", "tennis.png"]
	# create numpy araay for wordcloud mask image
	mask = np.array(Image.open(path.join(currdir, secrets.choice(imgs))))

	# create set of stopwords	
	stopwords = set(STOPWORDS)

	max_num = random.randint(1, 1001)*5

	# create wordcloud object
	wc = WordCloud(background_color="black",
					max_words=max_num, 
					mask=mask,
	               	stopwords=stopwords)
	
	# generate wordcloud
	wc.generate(text)

	# save wordcloud
	wc.to_file(path.join(currdir, "result.png"))


if __name__ == "__main__":
	# get query
	query = sys.argv[1]

	# get text for given query
	text = get_result(query)
	
	# generate wordcloud
	create_wordcloud(text)
