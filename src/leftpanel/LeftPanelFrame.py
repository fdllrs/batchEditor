import tkinter as tk
from tkinter import ttk
from leftpanel.InfoWidget import InfoWidget
from tkinter.filedialog import askdirectory

class LeftPanelFrame(tk.Frame):
      
      
      
    def __init__(self, root):
        super().__init__(root)
        


        
        self.createInfoWidget()
        self.createSelectDirWidget()




    def createInfoWidget(self):
        self.infoWidget = InfoWidget(self)
        self.infoWidget.grid(column=0, row=4, columnspan=5, sticky=tk.W)
       



    def createSelectDirWidget(self):

        self.rootDirectoryPath = tk.StringVar(value="no directory selected")
        self.minDurationMinutes = tk.DoubleVar(value=2)
        
        ttk.Button(self, text="select root directory", command=self.updateRootDir).grid(column=0, row=1, sticky=tk.W)
        ttk.Entry(self,  width=40, state='readonly', textvariable=self.rootDirectoryPath).grid(
            column=0, columnspan=3, row=2, sticky=tk.W)
        
        ttk.Label(self, text="edit any video file longer than: ").grid(column=0, row=3)
        
        ttk.Spinbox(self, from_=0.0, to=120.0, increment=0.5, width=5,
                     textvariable=self.minDurationMinutes, 
                     command=self.updateToEditVideoFiles
                     ).grid(column=1, row=3)
        
        ttk.Label(self, text="minutes").grid(column=2, row=3)

    def updateToEditVideoFiles(self):
        self.infoWidget.updateToEditVideoFiles(self.minDurationMinutes.get())
   
    def updateRootDir(self):
        dir = askdirectory()

        self.infoWidget.resetInfo()
        self.rootDirectoryPath.set(dir)
        self.infoWidget.updateInfo(dir)
        self.updateToEditVideoFiles()

