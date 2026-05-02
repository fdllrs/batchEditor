import subprocess
import cv2
from PySide6 import QtCore

def total_duration(listOfDurations):
    duration_minutes = sum(listOfDurations.values())

    return format_duration(duration_minutes)


def video_length(path: str):
    video = cv2.VideoCapture(path)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()

    return frame_count / fps


def audio_track_count(path) -> int:
    """Return the number of audio streams in a video file via ffprobe.

    Falls back to 1 if ffprobe is unavailable or the probe fails.
    """
    try:
        kwargs = {}
        if hasattr(subprocess, 'CREATE_NO_WINDOW'):
            kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW

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
            **kwargs
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


def get_auto_editor_path() -> str:
    """Return the currently configured path to the auto-editor executable."""
    settings = QtCore.QSettings("fdllrs", "BatchEditor")
    return str(settings.value("auto_editor_path", "auto-editor"))


def get_auto_editor_version(exe_path: str):
    """Execute 'auto-editor --version' and return the process result."""
    cmd = [exe_path, "--version"]
    kwargs = {}
    if hasattr(subprocess, 'CREATE_NO_WINDOW'):
        kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW

    return subprocess.run(
        cmd,
        capture_output=True,
        timeout=10,
        text=True,
        **kwargs
    )


