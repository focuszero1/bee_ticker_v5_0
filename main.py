# main.py - Bee Ticker v5.1 main entry point

import tkinter as tk
from datetime import datetime
from feeds import get_articles
from storage import load_saved_articles
from themes import apply_light_mode, apply_dark_mode
from gui import build_gui
from utils import format_time

def main():
    window = tk.Tk()
    window.title("Bee News Ticker v5.1")
    window.geometry("320x600")
    window.minsize(220, 400)

    style = tk.ttk.Style()
    style.configure("TButton", padding=6, relief="flat", background="#ccc")

    saved_articles = load_saved_articles() or []
    build_gui(window, saved_articles)

    window.mainloop()

if __name__ == "__main__":
    main()
