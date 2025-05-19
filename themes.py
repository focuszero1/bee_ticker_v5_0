# themes.py - Bee Ticker v5.4.1 polished themes module

from tkinter.ttk import Style, Button, Frame, Label

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

class App:
    def __init__(self, root):
        self.root = root
        self.style = Style(root)
        
        # Default to light mode
        apply_light_mode(self.style)
        
        # Theme toggle button
        self.is_light_mode = True

    def create_shell(self):
        # --- Top bar (buttons, controls) ---
        self.top_bar = Frame(self.root)
        self.top_bar.pack(side="top", fill="x", pady=2)

        # Remove or comment out any theme button creation here!
        # For example, if you have:
        # theme_button = Button(self.top_bar, text="Toggle Theme", command=self.toggle_theme)
        # theme_button.pack(side="right", padx=5)

        # --- Status bar (weather info, clock) ---
        self.status_bar = Frame(self.root)
        self.status_bar.pack(side="top", fill="x", pady=2)

        self.clock_label = Label(self.status_bar, text="")
        self.clock_label.pack(side="right", padx=5)

        # --- Main content area (feeds, saved articles) ---
        self.content_area = Frame(self.root)
        self.content_area.pack(fill="both", expand=True, padx=5, pady=5)

        # --- Bottom bar (reserved for future use) ---
        self.bottom_bar = Frame(self.root)
        self.bottom_bar.pack(side="bottom", fill="x", pady=2)
