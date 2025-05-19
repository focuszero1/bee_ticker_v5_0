# storage.py - Bee Ticker v5.5.2 with Discord integration

import json
import os
import requests
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

def send_to_discord(title: str, link: str, source: str) -> None:
    """Send a starred article to a Discord channel via webhook."""
    try:
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        webhook_url = config.get("DISCORD_WEBHOOK_URL")
        if not webhook_url:
            return  # No webhook configured

        payload = {
            "content": f"⭐ **New Saved Article:**\n**{title}** — *{source}*\n{link}"
        }
        requests.post(webhook_url, json=payload, timeout=3)
    except Exception as e:
        print("Failed to send to Discord:", e)

def toggle_save(title: str, link: str, source: str) -> None:
    """Toggle an article between saved and unsaved."""
    article = (title, link, source)
    if article in saved_articles:
        saved_articles.remove(article)
    else:
        saved_articles.append(article)
        send_to_discord(title, link, source)
    save_saved_articles()

def is_saved(title: str, link: str, source: str) -> bool:
    """Check if an article is currently saved."""
    return (title, link, source) in saved_articles

load_saved_articles()
