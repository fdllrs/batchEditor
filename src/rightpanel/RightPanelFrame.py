
import tkinter as tk
from tkinter import ttk

class RightPanelFrame(tk.Frame):
      
      
      
    def __init__(self, root):
        super().__init__(root)
        

        self.organizeIntoFolders = tk.BooleanVar(value=False)
        self.minDurationMinutes = tk.IntVar(value=2)




        ttk.Label(self, text="options").grid(column=0, row=2, columnspan=2)

        ttk.Checkbutton(self, text='Organize video files into folders',
            onvalue=True, offvalue=False, variable=self.organizeIntoFolders).grid(column=0, row=3)