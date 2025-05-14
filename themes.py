# themes.py - Bee Ticker v5.4.1 polished themes module

from tkinter.ttk import Style

def apply_light_mode(style: Style) -> None:
    """
    Apply light mode theme to the app.

    Args:
        style (Style): The ttk Style instance of the app.
    """
    style.configure(".", background="white", foreground="black", font=("Arial", 10))
    style.configure("TButton", background="white", foreground="black")
    style.configure("TLabel", background="white", foreground="black")

def apply_dark_mode(style: Style) -> None:
    """
    Apply dark mode theme to the app.

    Args:
        style (Style): The ttk Style instance of the app.
    """
    style.configure(".", background="#1e1e1e", foreground="#d0d0d0", font=("Arial", 10))
    style.configure("TButton", background="#1e1e1e", foreground="#d0d0d0")
    style.configure("TLabel", background="#1e1e1e", foreground="#d0d0d0")
