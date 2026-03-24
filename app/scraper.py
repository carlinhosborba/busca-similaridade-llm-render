import requests
from bs4 import BeautifulSoup

URLS = [
    "https://www.ibm.com/br-pt/think/topics/supervised-learning",
    "https://www.ibm.com/br-pt/think/topics/unsupervised-learning",
    "https://aws.amazon.com/pt/compare/the-difference-between-machine-learning-supervised-and-unsupervised/",
    "https://www.alura.com.br/artigos/machine-learning",
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