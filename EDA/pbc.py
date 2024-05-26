import pandas as pd
from scipy.stats import pointbiserialr

df = pd.read_csv(r'D:\Project2\Data\train.csv', header=None)
word_counts = df[2].apply(lambda x: len(str(x).split()))
data = pd.DataFrame({'Label': df[0], 'Word_Count': word_counts})
data['Label_Binary'] = data['Label'].apply(lambda x: 1 if x == 2 else 0)

correlation, p_value = pointbiserialr(data['Label_Binary'], data['Word_Count'])

print("Point Biserial Correlation:", correlation)
print("P-value:", p_value)
