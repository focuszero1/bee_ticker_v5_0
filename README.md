# Bee Ticker: Windows Edition

**Version:** v5.6  
**Platform:** Widnows (Tkinter GUI, ttkbootstrap)  
**Purpose:** A lightweight, auto-refreshing desktop dashboard that displays weather updates and beekeeping news headlines on a Pi touchscreen or small monitor.

---

## Features

- 🐝 **News Feeds:** Scrolls through live beekeeping-related RSS headlines (Google News, Bee Culture, American Bee Journal).
- 🌦 **Weather Panel:** Fetches and displays current weather conditions using OpenWeatherMap.
- ⭐ **Save Links:** Star and save interesting articles for later reading.
- 🖥 **Simple GUI:** Built with `tkinter` and `ttkbootstrap`, with light/dark mode toggle and clock.
- 📤 **Send-to-PC (Planned):** Will support pushing links to a shared file or endpoint.
- 🔄 **Auto-Refresh:** Feeds and weather update automatically at set intervals.
- 🌓 **Theme Toggle:** Switch between light and dark modes.

---

## Modules

- `main.py` — Launches the app with feeds and saved article views.
- `app_shell.py` — Main GUI container with frame swapping and theming.
- `feeds.py` — Handles RSS feed loading, display, and saving.
- `weather.py` — Queries OpenWeatherMap and updates GUI.
- `storage.py` — Manages saved articles locally in JSON.
- `utils.py` — Time formatting helpers.
- `themes.py` — Light/dark UI styles.
- `config.json` — Your API keys and settings (see below).

---

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/glitch-bee/bee_ticker.git
    cd bee_ticker
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure API keys:**
    - Copy `config.template.json` to `config.json`.
    - Fill in your [OpenWeatherMap API key](https://openweathermap.org/api) and (optionally) Discord webhook URL.

4. **(Optional) Add Weather Icons:**
    - Place PNG icons in an `icons/` folder if you want weather icons.

5. **Run the app:**
    ```bash
    python main.py
    ```

---

## Example `config.json`

```json
{
    "OPENWEATHER_API_KEY": "YOUR_API_KEY_HERE",
    "DISCORD_WEBHOOK_URL": ""
}
```

---

## Requirements

See `requirements.txt` for Python dependencies.

---

## Screenshots

![Bee Ticker Screenshot](screenshot.png)

---

## License

This project is for personal use.  
Weather icons and news feeds are subject to their respective licenses.

---

## Credits

- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)
- [feedparser](https://github.com/kurtmckee/feedparser)
- [OpenWeatherMap](https://openweathermap.org/)
