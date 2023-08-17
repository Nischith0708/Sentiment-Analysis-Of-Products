# Sentiment-Analysis-On-Products Reviews

![Sentiment Analysis](sentiment.png)

## Introduction

In today's competitive market, understanding customer sentiment is crucial for making informed strategic decisions. This project focuses on performing sentiment analysis on customer reviews of a dandruff removal hair product. By analyzing customer sentiments, product managers can gain valuable insights into customer preferences and concerns, helping them enhance the product's features and marketing strategies.

## Objective

The primary objective of this project is to develop a sentiment analysis model that accurately classifies customer reviews of a dandruff removal hair product as positive, negative, or neutral. The project provides actionable insights for product managers to make data-driven decisions.

## Methodology

### Data Collection
A dataset of customer reviews for the dandruff removal hair product was collected. Each review was stored in a CSV file with a single column containing the text of the review.

### Data Preprocessing
Text data preprocessing involved several steps:
- Removal of punctuation and special characters
- Lowercasing of text
- Tokenization
- Stopword removal
- Lemmatization

### Sentiment Analysis Model
A sentiment analysis model was developed using the preprocessed data. The `TextBlob` library was used for its simplicity and effectiveness.

### Model Evaluation
The trained sentiment analysis model was evaluated using metrics such as accuracy, precision, recall, and F1-score.

## Implementation

### Sentiment Analysis Code
The `sentiment_analysis.py` script performs sentiment analysis on customer reviews using the `TextBlob` library. It classifies reviews as positive, negative, or neutral and saves the results to a CSV file.

### Analysis and Insights
The `analysis_and_insights.ipynb` notebook analyzes sentiment distribution, sentiment trends over time (if date information is available), and creates word clouds for positive, negative, and neutral reviews.

## Usage

1. Frameworks Used: `Pandas, textblob, matplotlib, seaborn, wordcloud`

2. Input data:
   - Create a CSV file for example `dandruff_reviews.csv` with customer reviews.
   - Ensure you have a column for review text.

3. Run sentiment analysis: Execute `sentiment_analysis.py` to perform sentiment analysis on the reviews and generate sentiment results.

4. Explore analysis: Open and run the `analysis_and_insights.py` to visualize sentiment distribution, trends, and word clouds.

## Conclusion

Sentiment analysis of customer reviews for the dandruff removal hair product provides actionable insights into customer perceptions. By implementing this project, product managers can make informed decisions to enhance the product's quality, marketing, and overall customer satisfaction.

## Future Enhancements

- Implement more advanced sentiment analysis techniques using deep learning models.
- Perform aspect-based sentiment analysis to identify specific features of the product customers like/dislike.
- Gather additional customer demographic data to analyze sentiment variations across different groups.




