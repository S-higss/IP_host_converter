import requests

def is_valid_url(url):
    try:
        response = requests.get(url)
        return response.status_code // 100 == 2
    except requests.exceptions.RequestException:
        return False