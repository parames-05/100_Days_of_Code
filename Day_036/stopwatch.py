import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.time = 0  # in seconds

        root.title("Stopwatch")
        root.geometry("250x180")
        root.config(padx=15, pady=15)

        self.label = tk.Label(root, text="00:00:00",
                              font=("Arial", 32), bg="#f0f0f0")
        self.label.pack(fill="x", pady=10)

        self.start_btn = tk.Button(root, text="Start", width=8,
                                   font=("Arial", 12), command=self.start)
        self.start_btn.pack(pady=3)

        self.pause_btn = tk.Button(root, text="Pause", width=8,
                                   font=("Arial", 12), command=self.pause)
        self.pause_btn.pack(pady=3)

        self.reset_btn = tk.Button(root, text="Reset", width=8,
                                   font=("Arial", 12), command=self.reset)
        self.reset_btn.pack(pady=3)

    def update(self):
        if self.running:
            self.time += 1
            self.label.config(text=self.format_time(self.time))
            self.root.after(1000, self.update)

    def format_time(self, secs):
        h = secs // 3600
        m = (secs % 3600) // 60
        s = secs % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")


root = tk.Tk()
app = Stopwatch(root)
root.mainloop()
