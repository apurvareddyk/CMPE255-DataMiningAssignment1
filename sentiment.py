#get sentiment of text using textblob
def get_sentiment(text):
    from textblob import TextBlob
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
    
#test sentiment
print(get_sentiment("I love this product!"))
print(get_sentiment("I hate this product!"))
print(get_sentiment("This product is bad"))