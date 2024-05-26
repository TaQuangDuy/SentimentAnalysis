import pandas as pd
from nltk.stem import WordNetLemmatizer
import re

# Read the test data
test_data_path = r'D:\NLP\SentimentalAnalysis\Data\test_data.csv'
test_df = pd.read_csv(test_data_path)

# Read the train data
train_data_path = r'D:\NLP\SentimentalAnalysis\Data\train_data.csv'
train_df = pd.read_csv(train_data_path)

stop_words = {'a', 'an',  'the', 'in', 'on', 'at',
              'to', 'is', 'are', 'was', 'were', 'it', 'that',
              'these', 'those','this'}

lemmatizer = WordNetLemmatizer()
clean_pattern = re.compile(r'[^a-zA-Z0-9\s]')
url_pattern = re.compile(r'https?://\S+|www\.\S+')
html_pattern = re.compile(r'<.*?>')
def preprocess_text(text):
    text = url_pattern.sub('', text)
    text = html_pattern.sub('', text)
    text = re.sub(clean_pattern, '', text)
    text = text.lower()
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

# Load the Parquet files
test_data = pd.read_parquet(r'D:\NLP\SentimentalAnalysis\Data\test-00000-of-00001.parquet')
train_data = pd.read_parquet(r'D:\NLP\SentimentalAnalysis\Data\train-00000-of-00001.parquet')

# Apply preprocessing to the text column
test_data['preprocessed_text'] = test_data['text'].apply(preprocess_text)
train_data['preprocessed_text'] = train_data['text'].apply(preprocess_text)

# Extract 'label' column from original DataFrames
test_labels = test_data['label']
train_labels = train_data['label']

# Create new DataFrames with 'label' and 'text' columns
preprocessed_test_data = pd.DataFrame({
    'label': test_labels,
    'text': test_data['preprocessed_text']
})

preprocessed_train_data = pd.DataFrame({
    'label': train_labels,
    'text': train_data['preprocessed_text']
})

# Save preprocessed data to CSV files
preprocessed_test_data.to_csv(r'D:\NLP\SentimentalAnalysis\Data\preprocessed_test_data.csv', index=False)
preprocessed_train_data.to_csv(r'D:\NLP\SentimentalAnalysis\Data\preprocessed_train_data.csv', index=False)
