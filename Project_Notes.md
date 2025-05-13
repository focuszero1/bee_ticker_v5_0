# Bee Ticker Project Notes

## Project: Bee Ticker
Modular beekeeping news + weather desktop app  
Python + tkinter + ttk + feedparser + OpenWeatherMap API

## Current Version
**v5.3**  
Date: 2025-05-13  
Status: Stable working modular build

## Folder Structure
bee_ticker
├── main.py → App launcher + controller
├── gui.py → GUI logic + window creation
├── feeds.py → RSS news pulling (Google News, Bee Culture, ABJ)
├── weather.py → Live weather API fetch (OpenWeather)
├── storage.py → Persistent saved articles system (JSON file)
├── themes.py → Light/Dark mode style functions
├── utils.py → Utilities (format_time etc.)
├── config.json → OpenWeather API key storage
├── saved_articles.json → Saved articles (persistent data)
├── .git/ (if repo started)
├── .vscode/ (VS Code stability settings)


## Current Features
- Modular architecture complete
- Fully functional GUI (tkinter + ttk)
- News ticker with multiple feed sources
- Persistent “Save for Later” star toggle system
- Light/Dark theme toggle (ttk style based)
- Mouse wheel scrolling support
- Live weather display + weather icon
- Packaged to standalone .exe with pyinstaller (local test)

## Known Stable Milestones
- v5.0 → Single file → full modular conversion
- v5.1 → Weather API externalized to config.json
- v5.2 → Weather + news integrated GUI
- v5.3 → Canvas + ttk hybrid GUI, dark mode fixed, persistent saved_articles system finalized

## Next Planned Work (future versions)
- v5.4 → Add weather city input (user location)
- v5.5 → Add editable multi-RSS feed manager
- v5.6 → Add saved article export feature
- v5.7 → Add notification alerts for keyword matches
- v5.8 → Move RSS URLs to editable config file
- v6.0 → Consider plugin-based modular expansion (if app grows much larger)

## Notes
This project is now fully structured and safe to scale.  
This file acts as the primary "resync document" if chat is lost or development is resumed later.  
Assistant understands project state as of v5.3 snapshot.


