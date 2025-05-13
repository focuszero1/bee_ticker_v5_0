# storage.py - Bee Ticker v5.0 module

import json
import os

SAVE_FILE = "saved_articles.json"
saved_articles = []

def load_saved_articles():
    global saved_articles
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            saved_articles = json.load(f)

def save_articles():
    with open(SAVE_FILE, "w") as f:
        json.dump(saved_articles, f)

def is_saved(title, link, source):
    return (title, link, source) in saved_articles

def toggle_save(title, link, source):
    if is_saved(title, link, source):
        saved_articles.remove((title, link, source))
    else:
        saved_articles.append((title, link, source))
    save_articles()


