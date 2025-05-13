# main.py - Bee Ticker v5.0 launcher

import tkinter as tk
from tkinter import ttk
import threading
import time
from datetime import datetime
from feeds import get_articles
from storage import load_saved_articles, saved_articles
from themes import apply_light_mode, apply_dark_mode
from gui import build_gui
from utils import format_time

def main():
    window = tk.Tk()
    window.title("Bee News Ticker v5.0")
    window.geometry("320x600")
    window.minsize(220, 400)

    style = ttk.Style()
    current_theme = {"mode": "light"}

    apply_light_mode(style)

    # set up the GUI + get references to widgets
    gui = build_gui(window, style, get_articles, saved_articles)

    def toggle_dark_mode():
        if current_theme["mode"] == "light":
            apply_dark_mode(style)
            current_theme["mode"] = "dark"
        else:
            apply_light_mode(style)
            current_theme["mode"] = "light"

    gui["dark_button"].config(command=toggle_dark_mode)

    def toggle_view():
        gui["view_saved"][0] = not gui["view_saved"][0]
        if gui["view_saved"][0]:
            gui["display_articles"](saved_articles)
            gui["view_button"].config(text="View News Feed")
        else:
            gui["display_articles"](get_articles())
            gui["view_button"].config(text="View Saved Articles")

    gui["view_button"].config(command=toggle_view)

    def update_time():
        now = datetime.now()
        gui["time_label"].config(text=format_time(now))
        window.after(60000, update_time)

    update_time()

    def refresh_articles():
        while True:
            if not gui["view_saved"][0]:
                gui["display_articles"](get_articles())
            time.sleep(1800)

    load_saved_articles()
    gui["display_articles"](get_articles())

    threading.Thread(target=refresh_articles, daemon=True).start()
    window.mainloop()

if __name__ == "__main__":
    main()


