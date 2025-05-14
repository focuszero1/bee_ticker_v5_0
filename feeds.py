# feeds.py - Bee Ticker v5.4.1 polished feeds module

import tkinter as tk
from tkinter import ttk
import webbrowser
from utils import format_time
from storage import is_saved, toggle_save
import feedparser

FEEDS = {
    "Google News": "https://news.google.com/rss/search?q=honeybee+OR+beekeeping&hl=en-US&gl=US&ceid=US:en",
    "Bee Culture": "https://www.beeculture.com/feed/",
    "American Bee Journal": "https://americanbeejournal.com/feed/"
}

def get_articles():
    articles = []
    for source, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.published if "published" in entry else "",
                "source": source
            })
    return articles

def create_feed_frame(app):
    frame = ttk.Frame(app)

    canvas = tk.Canvas(frame, borderwidth=0)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Mousewheel scroll support (Windows/Mac/Linux compatible)
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    scrollable_frame.bind_all("<MouseWheel>", _on_mousewheel)

    # Populate articles
    articles = get_articles()
    for article in articles:
        article_frame = ttk.Frame(scrollable_frame, padding=(5, 3))
        article_frame.pack(fill="x", pady=2)

        title = article["title"]
        link = article["link"]
        published = article["published"]

        # Headline link label
        link_label = ttk.Label(
            article_frame,
            text=title,
            cursor="hand2",
            wraplength=240,
            justify="left"
        )
        link_label.pack(side="left", fill="x", expand=True, padx=5)
        link_label.bind("<Button-1>", lambda e, url=link: webbrowser.open_new(url))

        # Published date
        published_label = ttk.Label(
            article_frame,
            text=format_time(published),
            width=8,
            anchor="e"
        )
        published_label.pack(side="left", padx=3)

        # Star button
        star_text = "★" if is_saved(link) else "☆"
        star_btn = ttk.Button(article_frame, text=star_text, width=2)
        star_btn.config(command=lambda url=link, btn=star_btn: toggle_star(url, btn))
        star_btn.pack(side="right", padx=5)

    return frame

def toggle_star(url, btn):
    toggle_save(url)
    btn.config(text="★" if is_saved(url) else "☆")
