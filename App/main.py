from flask import Flask, request, render_template, redirect, url_for
from get_links import get_popular_links
from get_reviews import get_reviews, get_soup

app = Flask(__name__)

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
            reviews = get_reviews(soup, max_reviews=5)  # Sửa đổi ở đây
            reviews_list.append(reviews)
        return render_template('customer_results.html', product_links=product_links, reviews_list=reviews_list)

    return render_template('customer.html')

@app.route('/saler', methods=['GET', 'POST'])
def saler():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return "No file"

        # Assume the rest of the code handles file processing and classification
        # appropriately as it's not part of the question

        return "File uploaded successfully!"

    return render_template('saler.html')

if __name__ == '__main__':
    app.run(debug=True)
