import tkinter as tk

def on_click():
    print('You clicked me!')

window = tk.Tk()

button = tk.Button(window, text='Hello World', command=on_click)
button.pack()

window.mainloop()