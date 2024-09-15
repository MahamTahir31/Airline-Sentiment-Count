import pandas as pd

df = pd.read_csv('Tweets.csv')

airline_sentiment_count = {}

col = df['airline_sentiment']

for entry in col:

    if entry in airline_sentiment_count:
        airline_sentiment_count[entry] += 1
    else:
        airline_sentiment_count[entry] = 1

# Print the populated dictionary
print(airline_sentiment_count)
