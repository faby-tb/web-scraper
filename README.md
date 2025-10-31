# 🔍 News Scraper & Data Visualizer

A **robust Python scraper** that collects news headlines from Hacker News, cleans the data, analyzes top domains, and visualizes text patterns with charts and word clouds.

## 🧩 Features
- Modular, class-based scraper for maintainability
- Fetches headlines and links from Hacker News
- Cleans titles and extracts top domains
- Visualizes data: bar chart of top domains & word cloud of frequent words
- Ready for further AI/ML integration (sentiment analysis, classification)

## 🛠️ Tech Stack
- Python 3.x
- Requests & BeautifulSoup4
- Pandas & Matplotlib
- WordCloud

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/faby-tb/web-scraper-insights-refined.git
cd web-scraper-insights-refined
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the scraper:
```bash
python scraper.py
```
4. Open `analyze.ipynb` to visualize the results.

## 📊 Example Visualizations

- Top 10 domains
- Word cloud of headlines

## 📂 Folder Structure
```
web-scraper-insights-refined/
│
├── scraper.py          # main scraper script
├── analyze.ipynb       # Jupyter notebook for analysis & visualization
├── data/               # scraped CSV files
├── visuals/            # screenshots or plots (optional)
├── requirements.txt
└── README.md
```

## ⚠️ Notes
- For educational use only; respect each website's terms of service.
- Designed to be extendable for AI/ML features (e.g., sentiment analysis).

