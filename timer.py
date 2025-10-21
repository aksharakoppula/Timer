import tkinter as tk
class Timer:
    def __init__ (self, root):
        self.minutes=45
        self.seconds=0
        self.root=root
        self.root.title("Timer")
        self.label = tk.Label(root, text=f"{self.minutes:02d}:{self.seconds:02d}")
        self.label.pack(pady=20)
        self.button = tk.Button(root, text='Start', command=self.start_timer, bg="pink")
        self.button.pack(pady=20)
        self.stopbutton = tk.Button(root, text='Stop', command=self.end, bg="lightblue")
        self.stopbutton.pack(pady=20)
        self.resetbutton = tk.Button(root, text='Reset', command=self.reset, bg="lightyellow")
        self.resetbutton.pack(pady=20)
        self.running=False
    def start_timer (self):
        if not self.running:
            self.running=True
            self.countdown()
    def countdown (self):
        if self.running:
            if self.seconds == 0:
                if self.minutes > 0:
                    self.minutes -= 1
                    self.seconds = 59
                else:
                    self.running = False
                    self.label.config(text="Time's Up!")
                    return
            else:
                self.seconds -= 1

            self.label.config(text=f"{self.minutes:02d}:{self.seconds:02d}")
            self.root.after(1000, self.countdown)
    def end (self):
        if self.running:
            self.running=False
    def reset (self):
        self.running=False
        self.seconds=0
        self.minutes=45
        self.label.config(text=f"{self.minutes:02d}:{self.seconds:02d}")


if __name__ == "__main__":
    root = tk.Tk()
    pomodoro_timer = Timer(root)
    root.mainloop()
