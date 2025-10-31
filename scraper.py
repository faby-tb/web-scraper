import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse
from collections import Counter

class HackerNewsScraper:
    def __init__(self, url="https://news.ycombinator.com/"):
        self.url = url
        self.titles = []
        self.links = []
        self.domains = []

    def fetch(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        self.titles = [item.text for item in soup.select(".titleline > a")]
        self.links = [item["href"] for item in soup.select(".titleline > a")]
        self.domains = [urlparse(link).netloc for link in self.links]

    def clean_data(self):
        df = self.to_dataframe()
        df["title_clean"] = df["title"].str.replace(r"[^a-zA-Z0-9 ]", "", regex=True).str.lower()
        return df

    def to_dataframe(self):
        return pd.DataFrame({
            "title": self.titles,
            "link": self.links,
            "domain": self.domains
        })

    def save_csv(self, filename="data/articles.csv"):
        df = self.to_dataframe()
        df.to_csv(filename, index=False)
        print(f"✅ Saved {len(df)} articles to {filename}")


if __name__ == "__main__":
    scraper = HackerNewsScraper()
    html = scraper.fetch()
    scraper.parse(html)
    df_clean = scraper.clean_data()
    scraper.save_csv()
    print("Top 10 domains:")
    print(df_clean["domain"].value_counts().head(10))
