# gui.py - Bee Ticker v5.0 module

import tkinter as tk
from tkinter import ttk
import webbrowser
from storage import is_saved, toggle_save

def build_gui(window, style, get_articles_func, saved_articles):
    view_saved = [False]

    dark_button = ttk.Button(window, text="Toggle Dark Mode")
    dark_button.pack(pady=(5, 0))

    view_button = ttk.Button(window, text="View Saved Articles")
    view_button.pack(pady=(0, 5))

    time_label = ttk.Label(window, text="Last update: --")
    time_label.pack(pady=(5, 5))

    canvas = tk.Canvas(window, highlightthickness=0)
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scroll_frame = ttk.Frame(canvas)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def display_articles(articles):
        for widget in scroll_frame.winfo_children():
            widget.destroy()

        for title, link, source in articles:
            frame = ttk.Frame(scroll_frame)
            frame.pack(fill="x", pady=5, padx=5)

            star_symbol = "⭐" if is_saved(title, link, source) else "☆"
            star = ttk.Button(frame, text=star_symbol, width=2,
                              command=lambda t=title, l=link, s=source: (toggle_save(t, l, s), display_articles(get_articles_func() if not view_saved[0] else saved_articles)))
            star.pack(side="right", padx=5)

            label = ttk.Label(frame, text=title, cursor="hand2", wraplength=220, justify="left")
            label.pack(side="left", fill="x", expand=True)
            label.bind("<Button-1>", lambda e, url=link: webbrowser.open(url))

            source_label = ttk.Label(scroll_frame, text=f"({source})", font=("Arial", 8, "italic"))
            source_label.pack(anchor="w", padx=25)

    return {
        "dark_button": dark_button,
        "view_button": view_button,
        "time_label": time_label,
        "display_articles": display_articles,
        "view_saved": view_saved
    }


