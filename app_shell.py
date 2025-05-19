# app_shell.py - Bee Ticker v5.4.1 + swap_content added for v5.5 modules

from ttkbootstrap import Window, Style, ttk
from ttkbootstrap.constants import *
from datetime import datetime
from themes import apply_light_mode, apply_dark_mode
from weather import get_current_weather
from PIL import Image, ImageTk  # Pillow library

TITLE_FONT = ("Arial", 10, "bold")
REGULAR_FONT = ("Arial", 10)
ITALIC_FONT = ("Arial", 8, "italic")

class BeeTickerApp(Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("Bee News Ticker")
        self.geometry("320x700")
        self.minsize(220, 400)

        # Use the built-in style property (do NOT assign to it)
        self.style.configure("Article.TFrame", background="#23272b")
        self.style.configure("Article.TLabel", background="#23272b", foreground="#fff")

        self.current_theme = "light"
        self.current_frame = None

        # --- Status bar (weather info, clock) ---
        self.status_bar = ttk.Frame(self)
        self.status_bar.pack(side="top", fill="x", pady=4)

        self.weather_icon_label = ttk.Label(self.status_bar)
        self.weather_icon_label.pack(side="left", padx=2)
        self.weather_label = ttk.Label(self.status_bar, text="Loading weather...", font=REGULAR_FONT)
        self.weather_label.pack(side="left", padx=8, pady=2)

        self.clock_label = ttk.Label(self.status_bar, text="", font=REGULAR_FONT)
        self.clock_label.pack(side="right", padx=8, pady=2)

        # --- Main content area (feeds, saved articles) ---
        self.content_area = ttk.Frame(self)
        self.content_area.pack(fill="both", expand=True, padx=8, pady=8)

        # --- Bottom bar (reserved for future use) ---
        self.bottom_bar = ttk.Frame(self)
        self.bottom_bar.pack(side="bottom", fill="x", pady=4)

        # Initialize with a default frame
        self.swap_content(self.create_feed_frame())

        # Start clock
        self.update_clock()

        # Update weather
        self.update_weather()  # <-- Add this line

    def create_shell(self):
        # --- Top bar (buttons, controls) ---
        self.top_bar = ttk.Frame(self)
        self.top_bar.pack(side="top", fill="x", pady=4)

    # --- Theme toggle ---
    def toggle_theme(self):
        if self.current_theme == "light":
            apply_dark_mode(self.style)
            self.current_theme = "dark"
        else:
            apply_light_mode(self.style)
            self.current_theme = "light"

    # --- Clock updater ---
    def update_clock(self):
        now = datetime.now().strftime("%I:%M:%S %p")
        self.clock_label.config(text=now)
        self.after(1000, self.update_clock)

    # --- Weather updater ---
    def update_weather(self):
        weather = get_current_weather("New York City")
        if weather:
            # Load the icon image
            icon_path = f"icons/{weather['icon']}.png"
            try:
                img = Image.open(icon_path).resize((24, 24))
                self.weather_icon = ImageTk.PhotoImage(img)
                self.weather_icon_label.config(image=self.weather_icon)
            except Exception:
                self.weather_icon_label.config(image="")  # fallback if icon missing

            self.weather_label.config(
                text=f"{weather['city']}: {weather['temp']}°F, {weather['condition']}"
            )
        else:
            self.weather_icon_label.config(image="")
            self.weather_label.config(text="Weather unavailable")
        self.after(1800000, self.update_weather)  # 30 minutes

    # --- Module attachment API ---
    def attach_top_bar(self, widget):
        widget.pack(in_=self.top_bar, side="left", padx=5)

    def attach_status_bar(self, widget):
        widget.pack(in_=self.status_bar, side="left", padx=5)

    def attach_content(self, widget):
        widget.pack(in_=self.content_area, fill="both", expand=True)

    def attach_bottom_bar(self, widget):
        widget.pack(in_=self.bottom_bar, side="left", padx=5)

    # --- v5.5 ADDITION: content swapper ---
    def swap_content(self, new_frame):
        """Replace content area with a new frame."""
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(in_=self.content_area, fill="both", expand=True)  # <-- pack into content_area

    def create_feed_frame(self):
        """Create a default feed frame."""
        frame = ttk.Frame(self.content_area)
        # Add widgets to the frame as needed
        return frame

if __name__ == "__main__":
    app = BeeTickerApp()
    app.mainloop()
