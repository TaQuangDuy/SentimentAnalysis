import requests
from bs4 import BeautifulSoup
import pandas as pd

custom_headers = {
    "Accept-language": "en-GB,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
}

def get_soup(url):
    response = requests.get(url, headers=custom_headers)

    if response.status_code != 200:
        print("Error in getting webpage")
        exit(-1)

    soup = BeautifulSoup(response.text, "lxml")
    return soup

def get_reviews(soup, max_reviews=5):
    review_elements = soup.select("div.review")

    scraped_reviews = []

    for i, review in enumerate(review_elements):
        if i >= max_reviews:
            break

        r_content_element = review.select_one("span.review-text")
        r_content = r_content_element.text.strip() if r_content_element else None

        scraped_reviews.append(r_content)

    return scraped_reviews[:max_reviews]  # Ensure only maximum of 5 reviews are returned


