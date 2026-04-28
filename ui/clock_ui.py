import tkinter as tk
import time
import math
from models.doubly_circular_linked_list import DoublyCircularLinkedList
from services.theme_manager import ThemeManager
from services.clock_drawer import ClockDrawer
from ui.stopwatch_ui import Stopwatch

class AnalogClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analog Clock - Doubly Circular Linked List")
        self.geometry("500x750")
        self.resizable(False, False)

        self.theme_manager = ThemeManager()
        colors = self.theme_manager.current_colors()
        self.configure(bg=colors["bg"])

        self.canvas_size = 400
        self.center_x = self.canvas_size // 2
        self.center_y = self.canvas_size // 2
        self.radius = 160

        self.positions = DoublyCircularLinkedList()
        self._init_data_structure()

        self.canvas = tk.Canvas(self, width=self.canvas_size, height=self.canvas_size, 
                                bg=colors["bg"], highlightthickness=0)
        self.canvas.pack(pady=20)

        self.drawer = ClockDrawer(self.canvas, self.radius, self.center_x, self.center_y, self.positions)

        self.digital_label = tk.Label(self, text="", font=("Courier", 18, "bold"), 
                                      bg=colors["bg"], fg=colors["text"])
        self.digital_label.pack()

        self.date_label = tk.Label(self, text="", font=("Helvetica", 12),
                                   bg=colors["bg"], fg=colors["text"])
        self.date_label.pack()

        self.theme_btn = tk.Button(self, text="Toggle Dark Mode", command=self.toggle_theme,
                                   bg="black", fg="black", font=("Helvetica", 10, "bold"), 
                                   relief=tk.FLAT, padx=10, pady=5, highlightbackground=colors["bg"])
        self.theme_btn.pack(pady=10)

        self.stopwatch = Stopwatch(self, colors)
        self.stopwatch.pack(pady=5)

        self.update_clock()

    def toggle_theme(self):
        """Switches the theme via the ThemeManager and updates UI."""
        colors = self.theme_manager.toggle()
        self.configure(bg=colors["bg"])
        self.canvas.configure(bg=colors["bg"])
        self.digital_label.configure(bg=colors["bg"], fg=colors["text"])
        self.date_label.configure(bg=colors["bg"], fg=colors["text"])
        
        self.stopwatch.update_colors(colors)

        btn_text = "Toggle Light Mode" if self.theme_manager.is_dark_mode else "Toggle Dark Mode"
        self.theme_btn.configure(text=btn_text, highlightbackground=colors["bg"])
        
        self.drawer.draw_face(colors)

    def _init_data_structure(self):
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            self.positions.append(i, angle)

    def update_clock(self):
        colors = self.theme_manager.current_colors()

        if not self.canvas.find_withtag("face"):
            self.drawer.draw_face(colors)

        current_time = time.localtime()
        s = current_time.tm_sec
        m = current_time.tm_min
        h = current_time.tm_hour % 12

        self.digital_label.config(text=time.strftime("%I:%M:%S %p"))
        self.date_label.config(text=time.strftime("%A, %B %d, %Y"))

        self.drawer.draw_hands(s, m, h, colors)

        self.after(1000, self.update_clock)
