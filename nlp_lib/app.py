#!/usr/bin/env python
import wikipedia
import textblob
import fire


# Let's summarise with wikipedia
def summarise_wiki(query):
    # Get the summary from wikipedia
    summary = wikipedia.summary(query, sentences=3)
    return summary


# Let's search with wikipedia
def search_wiki(query):
    # Get the search results from wikipedia
    search_results = wikipedia.search(query)
    return search_results


# let's get the sentiment
def get_sentiment(query):
    # Get the sentiment from textblob
    sentiment = textblob.TextBlob(query).sentiment
    return sentiment


# let's get the tags
def get_tags(query):
    # Get the tags from textblob
    tags = textblob.TextBlob(query).tags
    return tags


# let's get the noun phrases
def get_noun_phrases(query):
    # Get the noun phrases from textblob
    noun_phrases = textblob.TextBlob(query).noun_phrases
    return noun_phrases


# lets run some tests
if __name__ == "__main__":
    fire.Fire(get_noun_phrases)
