from flask import Flask, request, render_template
from get_links import get_popular_links
from get_reviews import get_reviews, get_soup
from load_model import SentimentClassifier

app = Flask(__name__)

classifier = SentimentClassifier("D:\\NLP\\SentimentAnalysis\\Model\\trained model")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        keyword = request.form['product_name']
        max_links = 10
        product_links = get_popular_links(keyword, max_links)
        reviews_list = []
        for link in product_links:
            soup = get_soup(link)
            reviews = get_reviews(soup, max_reviews=5)
            average_score = classifier.classify_reviews(reviews)
            reviews_list.append((link, reviews, average_score))
        return render_template('customer_results.html', product_links=product_links, reviews_list=reviews_list)
    return render_template('customer.html')

@app.route('/saler', methods=['GET', 'POST'])
def saler():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return "No file"
        return "File uploaded successfully!"
    return render_template('saler.html')

if __name__ == '__main__':
    app.run(debug=True)
