import tkinter as tk


class GreetInfoFrame(tk.Frame):
    """Models the greeting information frame at the left window"""
    
    def __init__(self, parent, *args, **kwargs):
        # Initialize the frame
        super().__init__(parent, *args, **kwargs)
        
        self.agenda_label = tk.Label(self, text='Agenda')
        
        self.agenda_label.grid(row=0, column=0)
