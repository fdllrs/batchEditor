import tkinter as tk
from tkinter import ttk

from pathlib import Path
from utils import *

VIDEOFORMATS= ("mp4", "mkv")


class InfoWidget(tk.Frame):

    def __init__(self, root):
        super().__init__(root)


       
        self.toEditLengthMinutes = tk.StringVar(value="00:00 min")
        self.toEditLength = 0

        self.videoFilesFound = {}
        self.videoFilesFoundAmount = tk.IntVar(value=0)

        self.videoFilesToEdit = {}
        self.videoFilesToEditAmount = tk.IntVar(value=0)



        ttk.Label(self, text="video files found: ").grid(column=0, row=0, sticky=tk.W)
        ttk.Label(self, textvariable=self.videoFilesFoundAmount).grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text="video files to edit: ").grid(column=0, row=1, sticky=tk.W)
        ttk.Label(self, textvariable=self.videoFilesToEditAmount).grid(column=1, row=1, sticky=tk.W)
        
        ttk.Label(self, text="total duration to edit: ").grid(column=0, row=2, sticky=tk.W)
        ttk.Label(self, textvariable=self.toEditLengthMinutes).grid(column=1, row=2, sticky=tk.W)

    def resetInfo(self):
        self.toEditLengthMinutes.set(value="00:00 min")
        self.toEditLength = 0

        self.videoFilesFound ={}
        self.videoFilesFoundAmount.set(0)

        self.videoFilesToEdit = {}
        self.videoFilesToEditAmount.set(0)


    def updateInfo(self, dir):
        self.searchVideoFiles(Path(dir))
        self.updateLabels()


    def searchVideoFiles(self, directoryPath: Path):

        directoryElements = directoryPath.iterdir()

        for item in directoryElements:
            if str(item).endswith(VIDEOFORMATS):
                self.addRecording(item)


            elif item.is_dir():
                self.searchVideoFiles(item)

    def updateLabels(self):
        self.videoFilesFoundAmount.set(len(self.videoFilesFound)) 
        self.toEditLengthMinutes.set(formatDuration(self.toEditLength))
        self.videoFilesToEditAmount.set(len(self.videoFilesToEdit))

    
    def addRecording(self, itemPath):

        duration = videoLength(itemPath)
        self.videoFilesFound[itemPath] = duration


    def updateToEditVideoFiles(self, newThreshholdMinutes):

        self.toEditLength = 0

        filtered_dict = {}

        newThreshholdSeconds = newThreshholdMinutes *60
        for file_path, duration in self.videoFilesFound.items():
            if duration > newThreshholdSeconds:
                filtered_dict[file_path] = duration
                self.toEditLength += duration

        
        self.videoFilesToEdit = filtered_dict
        
        self.updateLabels()

