# Text analytics on MPP
Collection of tutorials/exercises for text analytics/NLP on the Pivotal MPP platform (Greenplum/HAWQ). 

## Vector space models

    1. Tokenization, stemming, unigrams, bigrams, trigram and skipgrams generation. 
    2. Bag-of-words model for classification on 20-news-groups dataset.
    3. tf-idf weighting for classification on 20-news-groups dataset.
    4. Feature hashing for classification on 20-news-groups dataset.
    5. Grid search on model parameters for Elastic Net on the  tf-idf representation

## Topic models

    1. LDA topic models on 20-news-groups dataset.
    2. Grid search for LDA hyperparameters, on the 20-news-groups dataset.

## Neural Language Models (Paragraph Vectors)

    1. Classification models using Paragraph vector representation of 20-news-groups dataset using `doc2vec` package in `gensim`.

## Dependencies

These exercises have the following client and server side dependencies:

1. Client side: We encourage you to install Anaconda Python for your Jupyter Notebooks. The notebooks in these exercises use matplotlib and seaborn for data visualization, pandas and psycopg2 to query the backend database.
2. Server side: On the server side, you'll need to install sklearn (and its dependencies).

### Note
These notebooks have been uploaded only to show code snippets, it is not meant to be a complete tutorial as is a narration that accompanies these exercises.
