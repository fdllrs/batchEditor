from bs4 import BeautifulSoup
import os
import cv2


def video_to_cv2(path: str):
    return cv2.VideoCapture(path)

def total_length_minutes(durations):
    return str(round(sum(durations.values()) / 60, 2))



def video_length(path: str):
    video = video_to_cv2(path)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()

    return frame_count / fps


def format_duration(duration_mins):
    return "{:02d}:{:02d} min".format(*divmod(int(duration_mins), 60))


def check_edited_length(path, i):

    file = open(f"{path}/{i}_ALTERED.xml", "r")
    i = 0
    for line in file:
        if i == 4:
            bs_data = BeautifulSoup(line, "lxml")
            length = int(bs_data.find("duration").text) / 60
            break
        i += 1
    return length
