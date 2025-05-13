# storage.py - Bee Ticker v5.4 master module

import json
import os

DATA_FILE = "saved_articles.json"
saved_articles = set()

def load_saved_articles():
    global saved_articles
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                articles = json.load(f)
                saved_articles = set(articles)
            except json.JSONDecodeError:
                saved_articles = set()
    else:
        saved_articles = set()

def save_saved_articles():
    with open(DATA_FILE, "w") as f:
        json.dump(list(saved_articles), f)

def toggle_save(url):
    if url in saved_articles:
        saved_articles.remove(url)
    else:
        saved_articles.add(url)
    save_saved_articles()

def is_saved(url):
    return url in saved_articles

# Load on import
load_saved_articles()
