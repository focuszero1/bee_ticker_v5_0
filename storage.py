# storage.py - Bee Ticker v5.4.1 polished storage module

import json
import os
from typing import List, Tuple

DATA_FILE = "saved_articles.json"
saved_articles: List[Tuple[str, str, str]] = []

def load_saved_articles() -> None:
    """Load saved articles (title, link, source) from the local JSON file into memory."""
    global saved_articles
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                articles = json.load(f)
                # Ensure each article is a tuple
                saved_articles = [tuple(article) for article in articles]
        except (json.JSONDecodeError, IOError):
            saved_articles = []
    else:
        saved_articles = []

def save_saved_articles() -> None:
    """Save the current list of saved articles to the local JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([list(article) for article in saved_articles], f, indent=2)
    except IOError:
        print("Error: Could not save articles to file.")

def toggle_save(title: str, link: str, source: str) -> None:
    """Toggle an article between saved and unsaved."""
    article = (title, link, source)
    if article in saved_articles:
        saved_articles.remove(article)
    else:
        saved_articles.append(article)
    save_saved_articles()

def is_saved(title: str, link: str, source: str) -> bool:
    """Check if an article is currently saved."""
    return (title, link, source) in saved_articles

# Load articles immediately when module is imported
load_saved_articles()
