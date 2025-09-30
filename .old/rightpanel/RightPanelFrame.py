
import tkinter as tk
from tkinter import ttk
from idlelib.tooltip import Hovertip

class RightPanelFrame(tk.Frame):
      
      
      
    def __init__(self, root):
        super().__init__(root)
        

        self.organizeIntoFolders = tk.BooleanVar(value=False)
        self.minDurationMinutes = tk.IntVar(value=2)
        self.preferredExportOption = tk.StringVar(value="Premiere Pro")
        self.threshold = tk.DoubleVar(value=6)

        ttk.Label(self, text="options").grid(column=0, row=0)

        ttk.Checkbutton(self, text='Organize video files into folders',
            onvalue=True, offvalue=False, variable=self.organizeIntoFolders).grid(column=0, row=1, columnspan=2, sticky=tk.W)
        # lbl = ttk.Button(self, text="?", state="disabled", width=1)
        # lbl.grid(column=3,row=1)
        # Hovertip(lbl, text="blalakblklblalalvl jajajak ajkja ka ajajaj hola \n ajskajajkajja hola lalaalalal", hover_delay=100)

        ttk.Label(self, text="preferred export option: ").grid(column=0, row=2, sticky=tk.W)
        ttk.Combobox(
            self, textvariable=self.preferredExportOption, values=["Premiere Pro", "Da Vinci Resolve", "XML"], state="readonly", width=12).grid(
                column=1, row=2, sticky=tk.W)
        
        self.sensitivityLabel = ttk.Label(self, text=f"threshold: {self.threshold.get()}%")
        self.sensitivityLabel.grid(column=0, row=3, sticky=tk.W)
        ttk.Scale(self, orient=tk.HORIZONTAL, length=97, from_=0, to=100, variable=self.threshold, command=self.updateSensitivityLabel).grid(column=1, row=3, sticky=tk.W, columnspan=2)

    def updateSensitivityLabel(self, value):
        self.sensitivityLabel.config(text=f"threshold: {round(float(value),2)}%")