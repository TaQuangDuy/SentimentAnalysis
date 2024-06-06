from get_links import get_popular_links
from get_reviews import get_reviews, get_soup

def test_get_links_and_reviews():
    keyword = "laptop"  # Thay đổi keyword nếu cần
    max_links = 5
    max_reviews_per_link = 5

    # Lấy danh sách các link sản phẩm phổ biến
    product_links = get_popular_links(keyword, max_links)

    # In ra các link để kiểm tra
    print("Product Links:")
    for link in product_links:
        print(link)

    # Lấy và in ra các đánh giá cho mỗi link sản phẩm
    for link in product_links:
        soup = get_soup(link)
        reviews = get_reviews(soup, max_reviews=max_reviews_per_link)
        print(f"\nReviews for {link}:")
        for i, review in enumerate(reviews, 1):
            print(f"Review {i}: {review}")

if __name__ == "__main__":
    test_get_links_and_reviews()
