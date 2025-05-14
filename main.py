# main.py - Bee Ticker v5.5.1.1 launcher

from tkinter import ttk
from app_shell import BeeTickerApp
from feeds import create_feed_frame, create_saved_frame

def main():
    app = BeeTickerApp()

    # Load initial feed frame
    feed_frame = create_feed_frame(app)
    app.attach_content(feed_frame)

    # Add Saved Articles button to top bar
    saved_btn = ttk.Button(
        text="View Saved",
        command=lambda: app.swap_content(create_saved_frame(app))
    )
    app.attach_top_bar(saved_btn)

    app.mainloop()

if __name__ == "__main__":
    main()
