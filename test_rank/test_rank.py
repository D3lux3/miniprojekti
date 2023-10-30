import os
import re
import csv
from nltk.stem.porter import *
import matplotlib.pyplot as plt

file_names = os.listdir("outputs2")

titles_and_views = []

for name in file_names:
    with open("outputs2/" + name, "r") as file:
        for line in file:
            segments = line.split(",")
            title = segments[1]
            views = re.sub(r"[^0-9]", "", segments[2])
            try:
                views = int(views)
            except:
                continue
            titles_and_views.append((title, views))

word_rank = {}

with open("eda/word_rank.csv", mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 2:
            key = row[0]
            value = float(row[1])
            word_rank[key] = value


def rank_title(input):
    input = re.sub(r"[^\w\s]", "", input.lower()) # remove punctuations and change to lower
    stemmed_words = [PorterStemmer().stem(word) for word in str(input).split()] # stemming
    return round(sum(word_rank.get(word, 0) for word in stemmed_words) / len(stemmed_words), 2)

views_ranks = []

for val in titles_and_views:
    views_ranks.append((val[1], rank_title(val[0])))

print(len(views_ranks))

x_values = [item[0] for item in views_ranks]
y_values = [item[1] for item in views_ranks]

plt.scatter(x_values, y_values)

plt.xlabel('Video views')
plt.ylabel('Video title ranks')

plt.show()
