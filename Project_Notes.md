# Bee Ticker Project Notes

## Project: Bee Ticker
Modular beekeeping news + weather desktop app  
Python + tkinter + ttk + feedparser + OpenWeatherMap API

## Current Version
**v5.5 candidate 1**  
Date: 2025-05-14  
Status: All modules polished, feeds fully functional, GUI cleanup phase started.

## Folder Structure
bee_ticker_v5_0/
├── app_shell.py → BeeTickerApp window shell
├── main.py → launcher only
├── feeds.py → scrollable news headlines
├── weather.py → weather data fetcher
├── storage.py → saved article persistence
├── themes.py → color + style themes
├── utils.py → helper functions (format_time)
├── config.json → externalized API key storage
├── saved_articles.json → persistent saved articles
├── .git/ → local Git repository
├── .vscode/ → VS Code local settings


## Current Features
- Modular architecture complete
- App runs via BeeTickerApp shell class
- Fully functional news feed pull + display
- Clickable article links open in browser
- Theme toggle (light/dark mode)
- Persistent saved articles system
- Clean modular project structure

## Known Stable Milestones
- **v5.0** → Single file → full modular conversion
- **v5.1** → Weather API externalized to config.json
- **v5.2** → Weather + news integrated GUI
- **v5.3** → Canvas + ttk hybrid GUI, saved_articles system finalized
- **v5.4** → Shell refactor + feeds module attached
- **v5.4.1** → Pre-polish stable pass
- **v5.5 candidate 1** → Major GUI improvement pass

## v5.4.1 Pre-Polish Functional Snapshot
**Date:** 2025-05-14

### Major Work Completed
**app_shell.py**
- Removed placeholder labels
- Added Theme toggle button
- Added persistent clock
- Polished main window shell structure

**feeds.py**
- Mousewheel scrolling fixed
- Padding + fonts improved
- Feed articles display fully functional
- Star toggle behavior working properly

**storage.py**
- Type hints + docstrings added
- Safer file read/write handling
- Human-readable saved JSON

**weather.py**
- Safer request handling with timeout
- Type hints + docstrings added
- Full compatibility with config.json
- Ready for shell integration

### Current App State
- Fully functional prototype
- All core modules cleaned + modernized
- Small visual polish bugs remain for later

### Next Planned Step
- Minor polish pass for themes.py
- Begin optional v5.4.2 refinements

## v5.5 Candidate 1 Snapshot
**Date:** 2025-05-14

### Major Work Completed
**feeds.py**
- Rebuilt for v5.5 candidate
- Added card-style borders + padding around articles
- Improved article label wrapping & fonts
- Fixed star button alignment
- Mousewheel scrolling fully stable
- Feeds display looks polished and professional

**Overall**
- Theme toggle + live clock continue working as expected
- Resizing + scroll behavior stable
- Dark mode works without issue
- No functional bugs; only minor visual polish ideas remain

### Status
- Marked as v5.5 candidate 1 internal stable checkpoint
- Ready to branch into next GUI refinement passes

### Next Steps
- Log polish bugs into v5.5 bugs list
- Optionally add Saved Articles view
- Tweak padding, font sizing, margins in next pass

v5.5 candidate 2 experimental:
- View Saved button and swap_content() test added.
- Saved articles display raw URLs only → not suitable for stable yet.
- Revert or rebuild saved_articles to match feeds/star system properly for candidate 3.
