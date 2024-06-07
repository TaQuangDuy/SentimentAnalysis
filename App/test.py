import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_soup(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error in getting webpage")
        exit(-1)
    soup = BeautifulSoup(response.text, "lxml")
    return soup

def get_reviews(soup):
    review_elements = soup.select("div.review")
    scraped_reviews = []
    for review in review_elements:
        r_author = review.select_one("span.a-profile-name").text.strip()
        r_rating = review.select_one("i.review-rating").text.strip().replace("out of 5 stars", "")
        r_title = review.select_one("a.review-title span:not([class])").text.strip()
        r_content = review.select_one("span.review-text").text.strip()
        r_date = review.select_one("span.review-date").text.strip()
        r_verified = review.select_one("span.a-size-mini").text.strip() if review.select_one("span.a-size-mini") else None
        r_image = review.select_one("img.review-image-tile")["src"] if review.select_one("img.review-image-tile") else None
        r = {
            "author": r_author,
            "rating": r_rating,
            "title": r_title,
            "content": r_content,
            "date": r_date,
            "verified": r_verified,
            "image_url": r_image
        }
        scraped_reviews.append(r)
    return scraped_reviews

def main():
    search_url = "https://www.amazon.com/BERIBES-Cancelling-Transparent-Soft-Earpads-Charging-Black/product-reviews/B0CDC4X65Q/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    soup = get_soup(search_url)
    data = get_reviews(soup)
    df = pd.DataFrame(data=data)
    df.to_csv("amz.csv", index=False)

if __name__ == '__main__':
    main()
