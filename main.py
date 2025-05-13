# main.py - Bee Ticker v5.4 master launcher

from app_shell import BeeTickerApp
from feeds import create_feed_frame

def main():
    app = BeeTickerApp()

    # Attach feeds module into content area
    feed_frame = create_feed_frame(app)
    app.attach_content(feed_frame)

    app.mainloop()

if __name__ == "__main__":
    main()