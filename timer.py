import tkinter as tk
class Timer:
    def __init__ (self, root):
        self.root=root
        self.root.title("Timer")
        self.label = tk.Label(root, text='Time:')
        self.label.pack(pady=20)
        self.button = tk.Button(root, text='Start', bg="pink")
        self.button.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    pomodoro_timer = Timer(root)
    root.mainloop()

