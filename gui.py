# gui.py – Bee Ticker v5.2 with live weather integration

import tkinter as tk
from tkinter import ttk
import requests
import io
from PIL import Image, ImageTk

from feeds import get_articles
from storage import load_saved_articles, save_articles
from themes import apply_light_mode, apply_dark_mode
from utils import format_time
from weather import get_current_weather

def build_gui(window, saved_articles):
    # ─── Theme & Colors ────────────────────────────────────────────
    current_colors = {
        "bg": "white",
        "fg": "black",
        "link": "blue",
        "button_bg": "white"
    }
    window.title("Bee Ticker")
    window.configure(bg=current_colors["bg"])

    # ─── Theme Toggle ───────────────────────────────────────────────
    def toggle_theme():
        if current_colors["bg"] == "white":
            apply_dark_mode(window, current_colors)
        else:
            apply_light_mode(window, current_colors)

    # ─── Article Refresh ────────────────────────────────────────────
    def refresh_articles():
        # clear existing
        for widget in news_frame.winfo_children():
            widget.destroy()

        # fetch & display
        articles = get_articles()
        for title, link, source in articles:
            row = tk.Frame(news_frame, bg=current_colors["bg"])
            row.pack(fill="x", padx=8, pady=(6, 2))

            link_label = tk.Label(
                row,
                text="- " + title,
                fg=current_colors["link"],
                bg=current_colors["bg"],
                cursor="hand2",
                wraplength=250,
                justify="left",
                font=("Arial", 10, "bold")
            )
            link_label.bind(
                "<Button-1>",
                lambda e, url=link: __import__("webbrowser").open(url)
            )
            link_label.pack(side="left", fill="x", expand=True)

            is_saved = (title, link, source) in saved_articles
            star_text = "★" if is_saved else "☆"
            def toggle_save(t=title, l=link, s=source, btn=None):
                if (t, l, s) in saved_articles:
                    saved_articles.remove((t, l, s))
                    btn.config(text="☆")
                else:
                    saved_articles.append((t, l, s))
                    btn.config(text="★")
                save_articles(saved_articles)

            star_btn = tk.Button(
                row,
                text=star_text,
                command=lambda t=title, l=link, s=source: toggle_save(t, l, s, star_btn),
                bg=current_colors["button_bg"],
                fg=current_colors["fg"],
                borderwidth=0
            )
            star_btn.pack(side="right")

            source_label = tk.Label(
                news_frame,
                text=f"({source})",
                fg=current_colors["fg"],
                bg=current_colors["bg"],
                font=("Arial", 8, "italic")
            )
            source_label.pack(anchor="w", padx=25)

        from datetime import datetime
        time_label.config(text=f"Last update: {format_time(datetime.now())}")


    # ─── View Saved Articles ─────────────────────────────────────────
    def view_saved():
        for widget in news_frame.winfo_children():
            widget.destroy()

        for title, link, source in saved_articles:
            row = tk.Frame(news_frame, bg=current_colors["bg"])
            row.pack(fill="x", padx=8, pady=(6, 2))

            link_label = tk.Label(
                row,
                text="- " + title,
                fg=current_colors["link"],
                bg=current_colors["bg"],
                cursor="hand2",
                wraplength=250,
                justify="left",
                font=("Arial", 10, "bold")
            )
            link_label.bind(
                "<Button-1>",
                lambda e, url=link: __import__("webbrowser").open(url)
            )
            link_label.pack(side="left", fill="x", expand=True)

            source_label = tk.Label(
                news_frame,
                text=f"({source})",
                fg=current_colors["fg"],
                bg=current_colors["bg"],
                font=("Arial", 8, "italic")
            )
            source_label.pack(anchor="w", padx=25)

        time_label.config(text="Viewing saved articles")

    # ─── GUI Controls ───────────────────────────────────────────────
    button_frame = tk.Frame(window, bg=current_colors["bg"])
    button_frame.pack(pady=(10, 5))
    tk.Button(button_frame, text="Toggle Dark Mode", command=toggle_theme).pack(side="left", padx=5)
    tk.Button(button_frame, text="View Saved Articles", command=view_saved).pack(side="left", padx=5)

    # ─── Weather Display ────────────────────────────────────────────
    weather_label = tk.Label(
        window,
        text="Current Weather: Loading…",
        font=("Arial", 10),
        bg=current_colors["bg"],
        fg=current_colors["fg"]
    )
    weather_label.pack(pady=(5, 2))

    weather_icon_label = tk.Label(window, bg=current_colors["bg"])
    weather_icon_label.pack(pady=(0, 5))

    def update_weather():
        data = get_current_weather("New York")  # or your default city
        if data:
            weather_label.config(
                text=f"Current Weather: {data['city']}: {data['temp']}°F, {data['condition']}"
            )
            icon_code = data.get("icon")
            if icon_code:
                try:
                    resp = requests.get(
                        f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
                    )
                    img = Image.open(io.BytesIO(resp.content)).resize((32, 32))
                    tk_img = ImageTk.PhotoImage(img)
                    weather_icon_label.config(image=tk_img)
                    weather_icon_label.image = tk_img  # keep reference
                except Exception as e:
                    print("Failed to load weather icon:", e)
        else:
            weather_label.config(text="Current Weather: data unavailable")

        window.after(600_000, update_weather)  # refresh in 10 min

    update_weather()

    # ─── News List ───────────────────────────────────────────────────
    time_label = tk.Label(
        window,
        text="",
        font=("Arial", 10),
        bg=current_colors["bg"],
        fg=current_colors["fg"]
    )
    time_label.pack()

    canvas = tk.Canvas(window, bg=current_colors["bg"])
    scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
    news_frame = tk.Frame(canvas, bg=current_colors["bg"])

    news_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=news_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    canvas.bind_all(
        "<MouseWheel>",
        lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    )

    refresh_articles()

if __name__ == "__main__":
    root = tk.Tk()
    saved = load_saved_articles()
    build_gui(root, saved)
    root.mainloop()
