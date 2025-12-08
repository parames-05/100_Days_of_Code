import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.time_left = 0
        self.running = False

        root.title("Quick Timers")
        root.geometry("300x280")
        root.config(padx=15, pady=15)

        self.label = tk.Label(root, text="00:00", font=("Arial", 40))
        self.label.pack(pady=10)

        # buttons row: predefined times
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        times = [
            ("30m", 30*60),
            ("15m", 15*60),
            ("10m", 10*60),
            ("5m",   5*60),
            ("1m",   60),
            ("30s",  30)
        ]

        for text, seconds in times:
            tk.Button(
                btn_frame, text=text, width=6,
                command=lambda s=seconds: self.start_timer(s)
            ).pack(side="left", padx=3)

        # Pause + Reset
        self.pause_btn = tk.Button(root, text="Pause", width=12,
                                   font=("Arial", 12), command=self.pause)
        self.pause_btn.pack(pady=3)

        self.reset_btn = tk.Button(root, text="Reset", width=12,
                                   font=("Arial", 12), command=self.reset)
        self.reset_btn.pack(pady=3)

    def format_time(self, secs):
        m = secs // 60
        s = secs % 60
        return f"{m:02d}:{s:02d}"

    def start_timer(self, seconds):
        self.pause()
        self.time_left = seconds
        self.label.config(text=self.format_time(self.time_left))
        self.running = True
        self.update_timer()

    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.label.config(text=self.format_time(self.time_left))
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0 and self.running:
            self.running = False
            self.label.config(text="Time!")

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time_left = 0
        self.label.config(text="00:00")


root = tk.Tk()
app = TimerApp(root)
root.mainloop()
