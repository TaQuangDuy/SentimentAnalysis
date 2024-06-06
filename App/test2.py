from main import app
import requests

def test_app_with_keyword(keyword):
    with app.test_client() as client:
        # Gửi request POST đến route /customer với từ khóa là "laptop"
        response = client.post('/customer', data={'product_name': keyword})
        # In ra response
        print(response.data.decode('utf-8'))

if __name__ == "__main__":
    keyword = "laptop"
    test_app_with_keyword(keyword)
