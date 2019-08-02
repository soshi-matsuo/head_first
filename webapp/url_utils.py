import requests

def gen_from_urls(urls: tuple) -> tuple:
    for res in (requests.get(url) for url in urls):
        yield len(res.content), res.status_code, res.url