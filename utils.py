# utils.py - Bee Ticker v5.4 master module

from datetime import datetime

def format_time(time_string):
    """Format RSS published time string into MM/DD format."""
    try:
        dt = datetime.strptime(time_string, "%a, %d %b %Y %H:%M:%S %z")
        return dt.strftime("%m/%d")
    except Exception:
        return ""
