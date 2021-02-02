import tkinter as tk

from frames.greet_info_frame import GreetInfoFrame


class Agenda(tk.Tk):
    """Models the Agenda GUI application window"""
    
    def __init__(self):
        # Initialize the window
        super().__init__()
        
        # Set window attributes
        self.title('Agenda')
        self.geometry('1200x800')
        self.resizable(width=False, height=False)
        
        # Create frames
        GreetInfoFrame(self).grid(row=0, column=0)


if __name__ == '__main__':
    agenda = Agenda()
    agenda.mainloop()