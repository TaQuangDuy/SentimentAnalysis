from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

class SentimentClassifier:
    def __init__(self, model_path):
        self.tokenizer = DistilBertTokenizer.from_pretrained(model_path)
        self.model = DistilBertForSequenceClassification.from_pretrained(model_path)

    def classify_reviews(self, reviews):
        inputs = self.tokenizer(reviews, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        predicted_labels = torch.argmax(outputs.logits, dim=1)
        average_score = predicted_labels.float().mean().item()
        return average_score
