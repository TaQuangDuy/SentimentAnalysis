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
def get_popular_links(keyword, max_links=10):
    base_url = f"https://www.amazon.com/s?k={keyword.replace(' ', '+')}"
    soup = get_soup(base_url)

    product_links = []
    link_elements = soup.select("h2 a.a-link-normal")
    for link_element in link_elements:
        product_links.append("https://www.amazon.com" + link_element["href"])
        if len(product_links) >= max_links:
            break

    return product_links

