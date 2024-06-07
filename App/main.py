from flask import Flask, request, render_template, redirect, url_for, flash
from get_links import get_popular_links
from get_reviews import get_reviews, get_soup
from load_model import SentimentClassifier
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = os.urandom(24)  # for flash messages

classifier = SentimentClassifier("D:\\NLP\\SentimentAnalysis\\Model\\trained model")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        keyword = request.form['product_name']
        if not keyword:
            flash('Product name is required', 'error')
            return redirect(url_for('customer'))
        try:
            max_links = 10
            product_links = get_popular_links(keyword, max_links)
            reviews_list = []
            for link in product_links:
                soup = get_soup(link)
                reviews = get_reviews(soup, max_reviews=5)
                if not reviews:
                    flash(f'No reviews found for link: {link}', 'error')
                    continue
                average_score = classifier.classify_reviews(reviews)
                reviews_list.append((link, average_score))

            # Sort the reviews_list by average_score in descending order and take the top 3
            reviews_list.sort(key=lambda x: x[1], reverse=True)
            top_reviews_list = reviews_list[:3]

            return render_template('customer_results.html', top_reviews_list=top_reviews_list)
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('customer'))
    return render_template('customer.html')


@app.route('/saler', methods=['GET', 'POST'])
def saler():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            flash('No file selected', 'error')
            return redirect(url_for('saler'))
        try:
            # Đọc tệp CSV
            df = pd.read_csv(file)
            reviews = df['review'].tolist()

            average_score = classifier.classify_reviews(reviews)

            flash(f'Average sentiment score for the uploaded reviews is: {average_score}', 'success')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')

        return redirect(url_for('saler'))
    return render_template('saler.html')

if __name__ == '__main__':
    app.run(debug=True)
