import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset with sentiment analysis results
data = pd.read_csv('dandruff_reviews_with_sentiment.csv')

# Sentiment Distribution
sentiment_counts = data['sentiment'].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
plt.title('Distribution of Sentiments in Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.show()

# Word Clouds for Positive, Negative, and Neutral Reviews
positive_reviews = ' '.join(data[data['sentiment'] == 'positive']['review_text'])
negative_reviews = ' '.join(data[data['sentiment'] == 'negative']['review_text'])
neutral_reviews = ' '.join(data[data['sentiment'] == 'neutral']['review_text'])

plt.figure(figsize=(10, 12))

plt.subplot(3, 1, 1)
wordcloud_positive = WordCloud(width=800, height=800, background_color='white').generate(positive_reviews)
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.title('Word Cloud - Positive Reviews')
plt.axis('off')

plt.subplot(3, 1, 2)
wordcloud_negative = WordCloud(width=800, height=800, background_color='white').generate(negative_reviews)
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.title('Word Cloud - Negative Reviews')
plt.axis('off')

plt.subplot(3, 1, 3)
wordcloud_neutral = WordCloud(width=800, height=800, background_color='white').generate(neutral_reviews)
plt.imshow(wordcloud_neutral, interpolation='bilinear')
plt.title('Word Cloud - Neutral Reviews')
plt.axis('off')

plt.tight_layout()
plt.show()
