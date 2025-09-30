import tkinter as tk
from tkinter import ttk
from leftpanel.LeftPanelFrame import LeftPanelFrame
from rightpanel.RightPanelFrame import RightPanelFrame
from utils import *




class App(tk.Tk):
   
    def __init__(self):
        self.configureRoot()
        self.createTitleWidget()
        self.createLeftPanel()
        self.createRightPanel()

    def configureRoot(self):
        super().__init__()
        self.title('Batch editor')
        self.geometry('600x200')
        self.minsize(600,150)

    def createTitleWidget(self):
        label = ttk.Label(self, text="Welcome to Batch Editor")
        label.grid(column=0, row=0, columnspan=7, sticky=tk.N)

    def createLeftPanel(self):
        leftPanelFrame = LeftPanelFrame(self)
        self.configurePanelFrame(leftPanelFrame, 0)

    def createRightPanel(self):
        rightPanelFrame = RightPanelFrame(self)
        self.configurePanelFrame(rightPanelFrame, 1)

    def configurePanelFrame(self, panelFrame: tk.Frame, col):
        panelFrame.config(relief="ridge", bd=5, width=300, height=150, padx=5, pady=5)
        panelFrame.grid_propagate(False) 
        panelFrame.grid(column=col, row=1, sticky=tk.W)


 
if __name__ == "__main__":
    app = App()
    app.mainloop()