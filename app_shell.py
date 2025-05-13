# app_shell.py - Bee Ticker v5.4 clean window shell

import tkinter as tk
from tkinter import ttk

class BeeTickerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bee News Ticker")
        self.geometry("320x600")
        self.minsize(220, 400)

        self.style = ttk.Style()

        # Create main layout shell
        self.create_shell()

    def create_shell(self):
        # --- Top bar (buttons, controls) ---
        self.top_bar = ttk.Frame(self)
        self.top_bar.pack(side="top", fill="x")

        # --- Status bar (weather info, etc.) ---
        self.status_bar = ttk.Frame(self)
        self.status_bar.pack(side="top", fill="x")

        # --- Main content area (feeds, saved articles) ---
        self.content_area = ttk.Frame(self)
        self.content_area.pack(fill="both", expand=True)

        # --- Bottom bar (optional future use) ---
        self.bottom_bar = ttk.Frame(self)
        self.bottom_bar.pack(side="bottom", fill="x")

        # Optional placeholder labels (remove later if you want)
        ttk.Label(self.top_bar, text="Top Bar").pack(padx=10, pady=5)
        ttk.Label(self.status_bar, text="Status/Weather Bar").pack(padx=10, pady=5)
        ttk.Label(self.content_area, text="Main Content Area").pack(padx=10, pady=30)
        ttk.Label(self.bottom_bar, text="Bottom Bar").pack(padx=10, pady=5)

    # --- Module attachment API ---

    def attach_top_bar(self, widget):
        widget.pack(in_=self.top_bar, side="left", padx=5)

    def attach_status_bar(self, widget):
        widget.pack(in_=self.status_bar, side="left", padx=5)

    def attach_content(self, widget):
        widget.pack(in_=self.content_area, fill="both", expand=True)

    def attach_bottom_bar(self, widget):
        widget.pack(in_=self.bottom_bar, side="left", padx=5)

if __name__ == "__main__":
    app = BeeTickerApp()
    app.mainloop()
