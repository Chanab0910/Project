import tkinter as tk


class TestGUI(tk.Frame):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self, master):
        super().__init__(master)
        self.Title = tk.Label(self, text='WORLD CUP PREDICTOR', font='Ariel 30 underline')
        self.Description = tk.Label(self, text='Please click on the flag that you would like to see the statistics of:',
                                    font='Helvetica 15')
        self.England_Flag = tk.PhotoImage(file='England_Flag.png')
        self.England_Button = tk.Button(self, image=self.England_Flag, width=100, height=65)

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.Title.grid(row=0, columnspan=5)
        self.Description.grid(row=1, columnspan=5)
        self.England_Button.grid(row=2, column=0)


if __name__ == '__main__':
    root = tk.Tk()
    main_frame = TestGUI(root)
    main_frame.pack()
    root.mainloop()
