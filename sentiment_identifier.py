import pandas as pd
from textblob import TextBlob

# Load the dataset
data = pd.read_csv('dandruff_reviews.csv')

# Perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment analysis to each review
data['sentiment'] = data['review_text'].apply(analyze_sentiment)

# Save the results back to CSV
data.to_csv('dandruff_reviews_with_sentiment.csv', index=False)

print("Sentiment analysis completed and results saved to 'dandruff_reviews_with_sentiment.csv'.")
