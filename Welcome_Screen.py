import tkinter as tk


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title = tk.Label(self, text='Hello World')


if __name__ == "__main__":
    menu = GUI()
    menu.mainloop()
