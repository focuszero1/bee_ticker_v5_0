# storage.py - Bee Ticker v5.4.1 polished storage module

import json
import os
from typing import Set

DATA_FILE = "saved_articles.json"
saved_articles: Set[str] = set()

def load_saved_articles() -> None:
    """Load saved article URLs from the local JSON file into memory."""
    global saved_articles
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                articles = json.load(f)
                saved_articles = set(articles)
        except (json.JSONDecodeError, IOError):
            saved_articles = set()
    else:
        saved_articles = set()

def save_saved_articles() -> None:
    """Save the current set of saved article URLs to the local JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(list(saved_articles), f, indent=2)
    except IOError:
        print("Error: Could not save articles to file.")

def toggle_save(url: str) -> None:
    """Toggle an article URL between saved and unsaved."""
    if url in saved_articles:
        saved_articles.remove(url)
    else:
        saved_articles.add(url)
    save_saved_articles()

def is_saved(url: str) -> bool:
    """Check if an article URL is currently saved."""
    return url in saved_articles

# Load articles immediately when module is imported
load_saved_articles()
