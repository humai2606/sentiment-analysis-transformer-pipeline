from transformers import pipeline

# Create sentiment analysis pipeline
sentiment = pipeline("sentiment-analysis")

# Get input from user
text = input("Enter a sentence: ")

# Perform sentiment analysis
result = sentiment(text)

# Display result
print("Sentiment:", result[0]["label"])
print("Confidence Score:", result[0]["score"])