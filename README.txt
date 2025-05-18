# Bee Ticker: Pi Mini App Edition

**Version**: v5.5.1.1  
**Platform**: Raspberry Pi (Tkinter GUI)  
**Purpose**: A lightweight, auto-refreshing desktop dashboard that displays weather updates and beekeeping news headlines on a Pi touchscreen or small monitor.

## Features

- 🐝 **News Feeds**: Scrolls through live beekeeping-related RSS headlines (Google News, Bee Culture, American Bee Journal).
- 🌦 **Weather Panel**: Fetches and displays current weather conditions using OpenWeatherMap.
- 💾 **Save Links**: Star and save interesting articles for later reading.
- 🖥 **Simple GUI**: Built with `tkinter`, with light/dark mode toggle and optional clock.
- 📤 **Send-to-PC (Planned)**: Will support pushing links to a shared file or endpoint.

## Current Modules

- `app_shell.py`: Main GUI container with frame swapping and theming
- `main.py`: Launches the app with feeds and saved article views
- `feeds.py`: Handles RSS feed loading, display, and saving
- `weather.py`: Queries OpenWeatherMap and updates GUI
- `storage.py`: Manages saved articles locally in JSON
- `utils.py`: Time formatting helpers
- `themes.py`: Light/dark UI styles

