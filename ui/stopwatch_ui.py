import tkinter as tk
import time

class Stopwatch(tk.Frame):
    def __init__(self, parent, colors):
        super().__init__(parent, bg=colors["bg"])
        
        self.running = False
        self.elapsed = 0
        self.last_time = 0

        self.label = tk.Label(self, text="00:00.0", font=("Courier", 16, "bold"), 
                              bg=colors["bg"], fg=colors["text"])
        self.label.pack(side=tk.TOP, pady=5)

        self.btn_frame = tk.Frame(self, bg=colors["bg"])
        self.btn_frame.pack(side=tk.TOP)

        self.start_resume_btn = tk.Button(self.btn_frame, text="Start", command=self.start_resume, highlightbackground=colors["bg"])
        self.start_resume_btn.pack(side=tk.LEFT, padx=5)

        self.pause_btn = tk.Button(self.btn_frame, text="Pause", command=self.pause, state=tk.DISABLED, highlightbackground=colors["bg"])
        self.pause_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = tk.Button(self.btn_frame, text="Reset", command=self.reset, highlightbackground=colors["bg"])
        self.reset_btn.pack(side=tk.LEFT, padx=5)

        self.update_timer()

    def update_colors(self, colors):
        self.configure(bg=colors["bg"])
        self.label.configure(bg=colors["bg"], fg=colors["text"])
        self.btn_frame.configure(bg=colors["bg"])
        
        self.start_resume_btn.configure(highlightbackground=colors["bg"])
        self.pause_btn.configure(highlightbackground=colors["bg"])
        self.reset_btn.configure(highlightbackground=colors["bg"])

    def start_resume(self):
        if not self.running:
            self.running = True
            self.last_time = time.time()
            self.start_resume_btn.config(state=tk.DISABLED)
            self.pause_btn.config(state=tk.NORMAL)
            
    def pause(self):
        if self.running:
            self.running = False
            self.start_resume_btn.config(state=tk.NORMAL, text="Resume")
            self.pause_btn.config(state=tk.DISABLED)

    def reset(self):
        self.running = False
        self.elapsed = 0
        self.label.config(text="00:00.0")
        self.start_resume_btn.config(state=tk.NORMAL, text="Start")
        self.pause_btn.config(state=tk.DISABLED)

    def update_timer(self):
        if self.running:
            now = time.time()
            self.elapsed += now - self.last_time
            self.last_time = now

            minutes = int(self.elapsed // 60)
            seconds = int(self.elapsed % 60)
            tenths = int((self.elapsed * 10) % 10)

            time_str = f"{minutes:02d}:{seconds:02d}.{tenths}"
            self.label.config(text=time_str)

        self.after(100, self.update_timer)
