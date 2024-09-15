# Sentiment Analysis of Airline Tweets

This code reads a CSV file containing tweets about airlines and counts the number of each sentiment type (e.g., positive, negative, neutral). The output is a dictionary that displays the sentiment counts.

## Prerequisites

Make sure you have Python installed on your system. This code requires the following Python packages:

- `pandas`

## Installation

1. **Clone the Repository (Optional):**
   If this code is part of a repository, clone it to your local machine:

   ```bash
   git clone https://github.com/MahamTahir31/Airline-Sentiment-Count
   ```

2. **Install Required Packages:**
   Install `pandas` using pip:

   ```bash
   pip install pandas
   ```

## Usage

1. Place your `Tweets.csv` file in the same directory as the script.

2. Run the code using the following command:

   ```bash
   python main.py
   ```

3. The code will read the `Tweets.csv` file, count the occurrences of each sentiment, and print the results to the console.


## Example Output

After running the code, the output will look like this:

```
{'neutral': 3099, 'positive': 2363, 'negative': 9178}
```
