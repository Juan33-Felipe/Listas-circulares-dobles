class ThemeManager:
    def __init__(self):
        self.is_dark_mode = False
        self.colors = {
            "light": {
                "bg": "#f0f0f5",
                "clock_bg": "#ffffff",
                "clock_border": "#2c3e50",
                "ticks": "#34495e",
                "hour_hand": "#2c3e50",
                "min_hand": "#7f8c8d",
                "sec_hand": "#e74c3c",
                "text": "#2c3e50"
            },
            "dark": {
                "bg": "#1a1a1a",
                "clock_bg": "#2d2d2d",
                "clock_border": "#ecf0f1",
                "ticks": "#bdc3c7",
                "hour_hand": "#ecf0f1",
                "min_hand": "#95a5a6",
                "sec_hand": "#e74c3c",
                "text": "#ecf0f1"
            }
        }

    def current_colors(self):
        return self.colors["dark"] if self.is_dark_mode else self.colors["light"]

    def toggle(self):
        self.is_dark_mode = not self.is_dark_mode
        return self.current_colors()
