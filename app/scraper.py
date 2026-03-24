import requests
from bs4 import BeautifulSoup

URLS = [
    "https://scikit-learn.org/stable/supervised_learning.html",
    "https://scikit-learn.org/stable/modules/clustering.html",
    "https://scikit-learn.org/stable/model_selection.html",
    "https://scikit-learn.org/stable/modules/feature_selection.html",
]

def fetch_page_text(url):
    response = requests.get(url, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)
    return text

def scrape_all():
    documents = []

    for url in URLS:
        try:
            text = fetch_page_text(url)
            documents.append({
                "url": url,
                "text": text
            })
        except Exception as e:
            print(f"Erro ao raspar {url}: {e}")

    return documents