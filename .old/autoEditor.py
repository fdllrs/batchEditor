import os
import subprocess
from utils import *

mainPath = "C:/Users/della/Videos/stam1o/videos/"


def autoEditor(video, recordingQuantity, start):
    totalEditedLength = 0
    totalLength = 0

    for i in range(start, recordingQuantity + start):

        videoPath = os.path.join(mainPath, video)
        recordingPath = os.path.join(videoPath, str(i))

        print(f"\nrecording {i}")
        if not os.path.exists(recordingPath):
            print(f"recording {i} no encontrado")
            continue

        # CHECK DURATION
        duration = videoLength(f"{os.path.join(recordingPath, str(i))}.mp4")

        totalLength += duration

        lst = os.listdir(recordingPath)
        toEdit = []
        edited = []
        # CHECK for mp4 longer than 60secs
        for file in lst:
            if (
                file.endswith("mp4")
                and videoLength(os.path.join(recordingPath, file)) > 60
            ):
                toEdit.append(file)

        # check if files are already edited
        for vid in toEdit:
            vidName = vid[:-4]
            if f"{vidName}_ALTERED.xml" in lst:
                print(f"- recording {vid} ya está procesado")
                edited.append(vid)

        organizeFolders(recordingPath, toEdit)
        for vid in toEdit:
            if vid not in edited:
                runcommand(recordingPath, vid)

        editedLength = checkEditedLength(recordingPath, i)
        totalEditedLength += editedLength

        printDuration("- duración original: ", duration)
        printDuration("- duración editado: ", editedLength)

    print("-----------------")

    printDuration("duración total: ", totalLength)
    printDuration("duración total editado: ", totalEditedLength)

    print(f"reducción del {round(100 - (totalEditedLength /totalLength *100),2)}%")


def runcommand(path, videoName):
    videoPath = os.path.join(path, str(videoName))
    autoEditorCommand = f'py -m auto_editor {videoPath} --margin 0.03sec --edit  "(or audio:stream=0 audio:threshold=0.7%, audio:stream=1 audio:threshold=2%, audio:stream=2 audio:threshold=1%)" --export premiere'
    try:
        subprocess.run(
            autoEditorCommand,
            cwd=path,
            check=True,
            text=True,
            encoding="utf-8",
        )

    except subprocess.CalledProcessError as e:
        print(f"Error in {path}: {e.stderr}")


def main():
    while True:
        videoName = input("nombre de la carpeta: ")
        if not os.path.exists(os.path.join(mainPath, videoName)):
            print("la carpeta no existe\n")
            continue

        crudos = len(os.listdir(os.path.join(mainPath, videoName)))

        quantity = input(f"cantidad de crudos ({crudos} detectados): ")

        if quantity == "":
            quantity = crudos

        if (
            not isinstance(int(quantity), int)
            or int(quantity) < 1
            or int(quantity) > crudos
        ):
            print("cantidad de crudos incorrecta")
            continue

        quantity = int(quantity)
        start = input(f"comenzar a partir de (default 0): ")

        if start == "":
            start = 0

        if not isinstance(int(start), int) or int(start) < 0:
            print(f"no es posible comenzar en el crudo {start}")
            continue

        start = int(start)

        break

    autoEditor(videoName, quantity, start)
    input("presiona enter para terminar.")


if __name__ == "__main__":
    main()
