
## Bee Ticker: Pi Mini App Edition (v1.0 Sketch)

**Core Goal**
A lightweight desktop app running on a Raspberry Pi with these essential functions:

* Show live local weather
* Scroll beekeeper news headlines
* Option to send interesting links from Pi to main computer for later reading

**Modules & Features**

1. **Weather Module**

* Pull local weather from OpenWeatherMap
* Show:

  * Current temperature
  * Conditions (clear, cloudy, raining, etc.)
  * Wind speed (optional)
  * Forecast snippet (optional)

2. **Feeds Module**

* Scroll beekeeper-related news headlines
* Clicking a headline opens in browser OR triggers a “send to PC” action
* Add “star/save” toggle to keep an article in a saved list on the Pi

3. **Send-to-PC Mechanism**

* Write URL to a shared file (`shared_links.txt` in a shared folder or SMB share)
  OR
* Push URL to a web endpoint on your main PC (basic local Flask or FastAPI service)
  OR
* Use MQTT to publish the link to a subscriber app on your PC

4. **System Features**

* Clean, simple tkinter interface
* Pi-friendly sizing for small monitor (or vertical display)
* Auto-start on boot

**Stretch Ideas (optional only if time permits)**

* Set refresh interval (e.g., weather every 30 mins, news every 10 mins)
* Add a small persistent clock
* Allow manual editing of `feeds.json` or `feeds.txt` to add new RSS feeds

**What NOT to build for v1.0**

* No full plugin system
* No external sensor integrations
* No complex config GUIs (use manual `config.json` for now)

**Summary**
This is a realistic “shippable to myself” milestone. It creates a practical, daily-use tool and provides a stable base for any future expansion.

## Folder and File Structure Ideas for Bee Ticker: Pi Mini App Edition

├── app_shell.py             # Main tkinter window + frame control
├── main.py                  # Launcher script (entry point)
├── config.json              # Stores API keys, feed URLs, settings
├── feeds.py                 # News feed logic + UI frame
├── weather.py               # Weather API fetch + UI frame
├── storage.py               # Saved articles and shared link handling
├── utils.py                 # Helper functions (e.g., format_time)
├── themes.py                # (Optional) Color and style settings (can remain shelved)
├── shared_links.txt         # (Optional) If using file-based send-to-PC method
├── saved_articles.json      # Stores saved articles
│
├── docs/                    # Project documentation
│   ├── architecture.md
│   ├── changelog.md
│   ├── ideas.md
│   ├── design/
│   └── screenshots/
│
├── sandbox/                 # (New) Experimental prototypes and drafts
│
├── .gitignore               # As you have it, possibly with sandbox exceptions
├── .vscode/                 # Local VS Code settings
├── requirements.txt         # Project dependencies for setup (optional)
├── README.txt               # Overview and usage instructions

