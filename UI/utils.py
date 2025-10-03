from bs4 import BeautifulSoup
import os
import cv2


def videoLength(path: str):
    video = cv2.VideoCapture(path)

    frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)

    return frameCount / fps


def formatDuration(durationMins):
    return "{:02d}:{:02d} min".format(*divmod(int(durationMins), 60))


def checkEditedLength(path, i):

    file = open(f"{path}/{i}_ALTERED.xml", "r")
    i = 0
    for line in file:
        if i == 4:
            Bs_data = BeautifulSoup(line, "lxml")
            length = int(Bs_data.find("duration").text) / 60
            break
        i += 1
    return length


def organizeFolders(path, toEdit):

    lst = os.listdir(path)

    if len(lst) == 1:
        print(f"- no hay replays ni screenshots")
        return
    # CHECK HOW MANY REPLAYS AND SCREENSHOTS
    replayQuantity = countReplays(toEdit, lst)
    screenshotQuantity = countScreenshots(toEdit, lst)
    # CREATE FOLDERS FOR REPLAYS AND/OR SCREENSHOTS
    createFolderFor(path, screenshotQuantity, "screenshots")
    createFolderFor(path, replayQuantity, "replays")

    # ORGANIZE REPLAYS AND/OR SCREENSHOTS
    organizeReplays(path, toEdit, lst)
    organizeScreenshots(path, toEdit, lst)


def organizeScreenshots(path, toEdit, lst):
    for file in lst:
        path_to_file = os.path.join(path, file)
        path_to_screenshot = os.path.join(path, "screenshots", file)

        if file in toEdit:
            continue

        if file.endswith((".jpg", ".jpeg", ".webp", ".png")):
            os.rename(path_to_file, os.path.join(path_to_file, path_to_screenshot))


def organizeReplays(path, toEdit, lst):
    for file in lst:
        path_to_file = os.path.join(path, file)
        path_to_replay = os.path.join(path, "replays", file)

        if file in toEdit:
            continue

        if file.endswith(".mp4"):
            os.rename(path_to_file, os.path.join(path_to_file, path_to_replay))


def countReplays(toEdit, lst):
    replayQuantity = 0
    for file in lst:
        if file in toEdit:
            continue
        if file.endswith(".mp4"):
            replayQuantity += 1

    return replayQuantity


def countScreenshots(toEdit, lst):
    screenshotQuantity = 0
    for file in lst:
        if file in toEdit:
            continue
        if file.endswith((".jpg", ".jpeg", ".webp", ".png")):
            screenshotQuantity += 1

    return screenshotQuantity


def createFolderFor(path, elements, folderName):
    if elements > 0:
        os.makedirs(os.path.join(path, folderName))
        print(f"- hay {elements} {folderName}")




