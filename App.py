import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import logging
import warnings

# Suppress the specific warning
warnings.filterwarnings("ignore", message="`resume_download` is deprecated.*")

# Model name

model_path = "D:\\NLP\\SentimentAnalysis\\Model\\trained model"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

def predict_sentiment(text):
    # Tokenize input text
    tokens = tokenizer(
        text,
        padding='max_length',
        truncation=True,
        max_length=512,
        return_tensors='pt'
    )

    input_ids = tokens.input_ids
    attention_mask = tokens.attention_mask
    model.eval()

    try:
        with torch.no_grad():
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1).squeeze().tolist()  # Convert to list
        predicted_label = torch.argmax(logits, dim=1).item()
    except Exception as e:
        logging.error(f"Error during model inference: {e}")
        raise

    # Adjust predicted label to match 1-5 star ratings
    predicted_label += 1

    return predicted_label, probabilities

def run_app():
    while True:
        # Get input text from the user
        user_input = input("Enter text (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Exiting...")
            break

        # Make a prediction
        try:
            label, probabilities = predict_sentiment(user_input)
            print(f"Predicted Rating: {label} stars")
            print(f"Predicted Probabilities: {probabilities}")
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            print("An error occurred during prediction. Please try again.")

# Run the app
if __name__ == "__main__":
    run_app()
