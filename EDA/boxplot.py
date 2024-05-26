import pandas as pd
import matplotlib.pyplot as plt
file_paths = [
    "D:/NLP/SentimentalAnalysis/Data/preprocessed_test_data.csv",
    "D:/NLP/SentimentalAnalysis/Data/preprocessed_train_data.csv"
]
dfs = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)
merged_df = pd.concat(dfs, ignore_index=True)
merged_df = merged_df.dropna(subset=['text'])
merged_df['word_count'] = merged_df['text'].apply(lambda x: len(str(x).split()))

plt.figure(figsize=(10, 6))
plt.boxplot(merged_df['word_count'], vert=False)
plt.title('Distribution of Word Count')
plt.ylabel('Word Count')
plt.show()
