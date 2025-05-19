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

## v5.6 Rebuild Plan (clean baseline)

**Date:** 2025-05-14

### Purpose

Stabilize core app after experimental v5.5.1.1 failure.
Remove unstable features and rebuild clean off `snapshot-v5.3`.
Focus is on functionality, not appearance polish.

### Rebuild Goals

* **Lock window size**

  * Hard-code fixed size (ex: 320x600 or 400x600)
  * Add `self.resizable(False, False)` in BeeTickerApp
  * Prevent resizing to eliminate floating button issues

* **Scrap dark mode / theme toggle**

  * Remove `themes.py` entirely
  * Remove `Toggle Theme` button
  * Set static neutral color scheme (ex: light grey or white background, black text)

* **Fix swap system**

  * Ensure `app.swap_content()` forcibly clears `content_area`
  * Ensure `create_feed_frame()` and `create_saved_frame()` return frames only
  * No more packing directly to `app`

* **Fix saved articles storage**

  * Redesign `storage.py` to store `(title, link, source)` tuple sets
  * Rewrite Saved Articles display to match main feed style
  * Eliminate raw URL display problem

* **Eliminate floating layouts**

  * Simplify all frame + button layouts
  * Avoid scrollable canvas inside Saved Articles
  * List saved articles as fixed cards just like feeds

* **Keep feeds + saved views only**

  * Do not add any experimental modules
  * `main.py` should attach Feeds by default with Saved button in top bar

* **Tag v5.6-dev only when stable**

  * This will become new clean baseline for all future feature work

### Outcome

v5.6 will restore stability and modularity, acting as the **new clean base milestone** for future features.

v5.5.2 (2025-05-15)
- Fixed saved articles displaying as URLs; now styled with title and source.
- Fixed 'Back to Feeds' navigation from Saved view.
- All user-facing bugs from v5.5 candidate 1 resolved.

from datetime import datetime
from pathlib import Path

# Define the snapshot text for Project_Notes.md
snapshot = f"""
## v5.6 Stable Baseline
**Date:** {datetime.today().strftime("%Y-%m-%d")}

### Overview
This version marks the first stable post-canvas rewrite baseline.

### Key Features
- Canvas removed from feeds and saved views
- No more mousewheel bindings or scroll glitches
- Theme toggle and clock functioning
- Article cards display cleanly with title, source, and star toggle
- All modules load without error

### Known Tradeoffs
- No saved articles view
- No scrolling or pagination (only visible articles shown)
- Minimal theming polish

### Next Potential Steps
- Add Refresh button
- Pagination for article sets
- Visual theme polish
- Pi Mini Mode (auto-launch, touch optimizations)

### Status
This version is clean, stable, and suitable as a base for all future development.
"""

# Path to update the file
notes_path = Path("/mnt/data/Project_Notes.md")

# Append the snapshot to the file
with open(notes_path, "a", encoding="utf-8") as f:
    f.write("\n" + snapshot.strip() + "\n")

# Return path for push reference
notes_path.name

## v5.6 Final Release
**Date:** 2025-05-19

### Key Features
- Clean architecture from v5.3 snapshot forward
- Feeds pull and render reliably using card-style layout
- Star toggle system works with local save and Discord integration
- Theme toggle and clock functional and stable
- Weather module fully functional via OpenWeatherMap API
- Mousewheel scrolling removed for stable sizing
- Local saving preserved but no saved view required

### Discord Integration
- New feature: star an article → instantly sent to Discord via webhook
- Can be enabled/disabled via `config.json`
- Replaces in-app saved article view and simplifies user flow

### Status
- All modules tested and functioning
- No known UI or performance bugs
- Ready for public/stable use as v5.6
