import tkinter as tk
from tkinter import ttk


class TestGUI(tk.Frame):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self, master):
        super().__init__(master)

        self.Space = tk.Label(self, text=' ',bg='white')
        self.Title = tk.Label(self, text='WORLD CUP PREDICTOR', font=('FuturaStd-Heavy',45), bg='white', pady=30)

        self.Description1 = tk.Label(self, text='Welcome to the World cup predictor. In this predictor, the World '
                                                'Cup has been simulated 1000 times, and you ', font = 'FuturaStd-Medium',bg='white', padx=50, pady=4, )

        self.Description2 = tk.Label(self, text='are able to see accurate chances of a range of possibilities '
                                                'happening. This can range from how many times', font = 'FuturaStd-Medium',bg='white', padx=50, pady=4)

        self.Description3 = tk.Label(self, text='they won the World Cup to the average amount of '
                                                'yellow cards per game.', font = 'FuturaStd-Medium',bg='white',padx=50, pady=4)

        self.Next_Page_Button = tk.Button(self, text='See Results',font = 'FuturaStd-Medium')
        self.quit = tk.Button(self, text='Quit',font = 'FuturaStd-Medium', command=quit)

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.Title.grid(row=0, columnspan=5)
        self.Description1.grid(row=1, columnspan=5)
        self.Description2.grid(row=2, columnspan=5)
        self.Description3.grid(row=3, columnspan=5)
        self.Space.grid(row=4,column=0)
        self.Space.grid(row=5, column=0)
        self.Next_Page_Button.grid(row = 6, column = 4)
        self.quit.grid(row = 6, column=0)

if __name__ == '__main__':
    root = tk.Tk()
    main_frame = TestGUI(root)
    main_frame.pack()
    main_frame.config(bg="white")
    root.mainloop()