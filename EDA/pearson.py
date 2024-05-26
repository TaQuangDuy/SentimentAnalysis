import pandas as pd
from scipy.stats import pearsonr

file_paths = [
    "D:/NLP/SentimentalAnalysis/Data/preprocessed_test_data.csv",
    "D:/NLP/SentimentalAnalysis/Data/preprocessed_train_data.csv"
]
dfs = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)
merged_df = merged_df.dropna(subset=['text', 'label'])
merged_df['word_count'] = merged_df['text'].apply(lambda x: len(str(x).split()))
merged_df['stars'] = merged_df['label'] + 1
pearson_corr, p_value = pearsonr(merged_df['word_count'], merged_df['stars'])
print("Pearson correlation coefficient:", pearson_corr)
print("p-value:", p_value)
