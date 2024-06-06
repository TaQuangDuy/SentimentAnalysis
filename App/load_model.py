from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

# Load the tokenizer and model
model_path = "D:\\NLP\\SentimentAnalysis\\Model\\trained model"
tokenizer = DistilBertTokenizer.from_pretrained(model_path)
model = DistilBertForSequenceClassification.from_pretrained(model_path)


def classify_reviews(reviews):
    # Tokenize the reviews
    inputs = tokenizer(reviews, padding=True, truncation=True, return_tensors="pt")

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted labels
    predicted_labels = torch.argmax(outputs.logits, dim=1)

    # Calculate the average score
    average_score = predicted_labels.float().mean().item()

    return average_score
