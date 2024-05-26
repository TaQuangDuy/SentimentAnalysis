import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from two CSV files
test_data = pd.read_csv('D:/NLP/SentimentalAnalysis/Data/preprocessed_test_data1.csv')
train_data = pd.read_csv('D:/NLP/SentimentalAnalysis/Data/preprocessed_train_data1.csv')

# Merge data from both files
merged_data = pd.concat([test_data, train_data])

# Calculate the word count for each sample
merged_data['word_count'] = merged_data['text'].apply(lambda x: len(str(x).split()))

# Calculate density
word_count_density = merged_data['word_count'].value_counts(normalize=True).sort_index()

# Plot the line chart
plt.figure(figsize=(10, 6))
sns.lineplot(x=word_count_density.index, y=word_count_density.values)
plt.title('Word Count Density')
plt.xlabel('Number of words per sample')
plt.ylabel('Density')
plt.grid(True)
plt.show()
plt.savefig('word_density_1')