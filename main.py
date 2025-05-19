# main.py - Bee Ticker v5.5.1.1 launcher

from app_shell import BeeTickerApp
from feeds import create_feed_frame

def main():
    app = BeeTickerApp()

    # Load initial feed frame
    feed_frame = create_feed_frame(app)
    app.swap_content(feed_frame)

    app.mainloop()

if __name__ == "__main__":
    main()
