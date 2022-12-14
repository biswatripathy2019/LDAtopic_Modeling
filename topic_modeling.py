# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zd8BUJ_MdzvEw4JzEQlfry0P8EfVIyee
"""

from google.colab import files
files.upload()

import pandas as pd
data=pd.read_csv('/content/lda_data.csv')
data.head()

data['headline_text'][20]

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer(max_df=0.8, min_df=2, stop_words='english')
doc_term_matrix = count_vect.fit_transform(data['headline_text'].values.astype('U'))

doc_term_matrix

from sklearn.decomposition import LatentDirichletAllocation

LDA = LatentDirichletAllocation(n_components=5, random_state=42)
LDA.fit(doc_term_matrix)

count_vect.get_feature_names()

import random

for i in range(10):
    random_id = random.randint(0,len(count_vect.get_feature_names()))
    #print(random_id)
    print(count_vect.get_feature_names()[random_id])

first_topic = LDA.components_[0]

first_topic

top_topic_words = first_topic.argsort()[-10:]

top_topic_words

for i in top_topic_words:
    print(count_vect.get_feature_names()[i])

for i,topic in enumerate(LDA.components_):
    print(f'Top 10 words for topic #{i}:')
    print([count_vect.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print('\n')

topic_values = LDA.transform(doc_term_matrix)
topic_values.shape

data['Topic'] = topic_values.argmax(axis=1)

data.to_csv('with level.csv')

#nmf not negetive matrix factorization
from sklearn.decomposition import NMF

nmf = NMF(n_components=5, random_state=42)
nmf.fit(doc_term_matrix )

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vect = TfidfVectorizer(max_df=0.8, min_df=2, stop_words='english')
doc_term_matrix = tfidf_vect.fit_transform(data['headline_text'].values.astype('U'))

import random

for i in range(10):
    random_id = random.randint(0,len(tfidf_vect.get_feature_names()))
    print(tfidf_vect.get_feature_names()[random_id])

first_topic = nmf.components_[0]
top_topic_words = first_topic.argsort()[-10:]

for i in top_topic_words:
    print(tfidf_vect.get_feature_names()[i])

for i,topic in enumerate(nmf.components_):
    print(f'Top 10 words for topic #{i}:')
    print([tfidf_vect.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print('\n')

topic_values = nmf.transform(doc_term_matrix)
data['Topic_NM'] = topic_values.argmax(axis=1)
data.to_csv('with_level_nm.csv')

