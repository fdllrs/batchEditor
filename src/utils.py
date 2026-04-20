from bs4 import BeautifulSoup
import os
import subprocess
import cv2
from pathlib import Path


def video_to_cv2(path: str):
    return cv2.VideoCapture(path)

def total_duration(listOfDurations):
    duration_minutes = sum(listOfDurations.values())

    return format_duration(duration_minutes)


def video_length(path: str):
    video = video_to_cv2(path)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()

    return frame_count / fps


def audio_track_count(path) -> int:
    """Return the number of audio streams in a video file via ffprobe.

    Falls back to 1 if ffprobe is unavailable or the probe fails.
    """
    try:
        result = subprocess.run(
            [
                "ffprobe", "-v", "error",
                "-select_streams", "a",
                "-show_entries", "stream=index",
                "-of", "csv=p=0",
                str(path),
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        lines = [ln for ln in result.stdout.splitlines() if ln.strip()]
        return max(len(lines), 1)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return 1


def format_duration(duration_secs):
    total_secs = int(duration_secs)
    hours, remainder = divmod(total_secs, 3600)
    mins, secs = divmod(remainder, 60)
    if hours > 0:
        return "{:d}:{:02d}:{:02d}".format(hours, mins, secs)
    return "{:02d}:{:02d}".format(mins, secs)


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
