from tkinter import *
import tkinter as tk

class Window:
    
    def __init__(self, width, height, title):
        self.window = Tk() # make window
        self.window.geometry(f'{width}x{height}')
        self.window.title(title)
    
    def display(self):
        self.window.mainloop()
    
    def create_components(self):
        header = Label(self.window, text='Endangered Species In Your State')
        header.place(x=10, y=10)
        header.pack()



