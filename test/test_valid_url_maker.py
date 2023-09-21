from src.url_maker import url_maker
from src.url_checker import is_valid_url

while True:
    hostname = str(input("input hostname: "))

    urls = url_maker(hostname)
    print(urls)
    
    valid_url = []

    for url in urls:
        if is_valid_url(url):
            valid_url.append(url)

    if valid_url:
        print(f"success: {valid_url}")
    else: print("failed")