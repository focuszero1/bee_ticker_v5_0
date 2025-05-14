# Bee Ticker Project Notes

## Project: Bee Ticker
Modular beekeeping news + weather desktop app  
Python + tkinter + ttk + feedparser + OpenWeatherMap API

## Current Version
**v5.4**  
Date: 2025-05-13  
Status: Shell + feeds working (needs visual cleanup)

## Folder Structure
bee_ticker_v5_0/
├── app_shell.py → BeeTickerApp window shell
├── main.py → launcher only
├── feeds.py → scrollable news headlines (attached)
├── weather.py → (pending reconnect)
├── storage.py → saved article persistence
├── themes.py → (currently shelved)
├── utils.py → helper functions (format_time)
├── config.json → externalized API key storage
├── saved_articles.json → persistent saved articles
├── .git/ → local Git repository fully initialized
├── .vscode/ → VS Code local virtual environment stability settings

## Current Features
- Modular architecture complete
- App runs via BeeTickerApp shell class
- Fully functional news feed pull + display
- Clickable article links open in browser
- Project structured for clean module attachments

## Known Stable Milestones
- v5.0 → Single file → full modular conversion
- v5.1 → Weather API externalized to config.json
- v5.2 → Weather + news integrated GUI
- v5.3 → Canvas + ttk hybrid GUI, persistent saved_articles system finalized
- v5.4 → Shell refactor milestone + feeds module attached
    - App refactored into BeeTickerApp shell class
    - main.py converted to launcher only
    - feeds module fully rewired into shell (create_feed_frame)
    - news headlines display working with live data pull
    - star toggle, scroll area, and visual layout remain incomplete for next phase

## Next Planned Work (future versions)
- v5.4.1 → Feeds polish (scroll fix, star button restore, remove placeholder labels)
- v5.5 → Add editable multi-RSS feed manager
- v5.6 → Add saved article export feature
- v5.7 → Add notification alerts for keyword matches
- v5.8 → Move RSS URLs to editable config file
- v6.0 → Consider plugin-based modular expansion (if app grows much larger)

## Notes
This project is fully structured and safe to continue scaling.  
This file remains the primary "resync document" for project continuation.  
Assistant understands project state as of v5.4 snapshot (shell + feeds working).

Bee Ticker v5.4.1 Pre-Polish Functional Snapshot
Date: 2025-05-14

Major Work Completed:
app_shell.py fully rewritten:

Removed placeholder labels

Added Theme toggle button

Added persistent clock

Polished main window shell structure

feeds.py fully rewritten:

Mousewheel scrolling fixed

Padding + fonts improved

Feed articles display fully functional

Star toggle behavior works properly

storage.py polished:

Type hints + docstrings added

Safer file read/write handling

Human-readable saved JSON

weather.py polished:

Safer request handling with timeout

Type hints + docstrings added

Full compatibility with config.json

Ready for shell integration

Current App State:
Fully functional prototype

All core modules cleaned + modernized

Small visual polish bugs remain for later (logged separately)

Next Planned Step:
Minor polish pass for themes.py

Begin v5.4.2 optional refinements