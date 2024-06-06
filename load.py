from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Model name
model_name = "zuyzuyyy/Fine-tune_BERT"

# Custom cache directory
cache_dir = r"D:\NLP\SentimentAnalysis"

# Download the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_name, cache_dir=cache_dir)