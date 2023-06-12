import requests

request = requests.post(
    "http://127.0.0.1:8000/contents/create/",
    json={"user_id": 5, "book_name": "as", "book_content": "adqwe", "book_page": 14}
)
print(request.status_code)
