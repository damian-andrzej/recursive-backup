#choose a folder to backup
import zipfile, os
import tkinter as tk
from tkinter import filedialog

def backupToZip():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    try:
        folder = filedialog.askdirectory()
        if folder:
            print("Selected folder:", folder)
            os.chdir(folder)
            folder = os.path.abspath(folder)
            number = 1
            while True:
                zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
                if not os.path.exists(zipFilename):
                    break
                number = number + 1
            # TODO Create a zip file
            newZip = zipfile.ZipFile(zipFilename, 'w')
            # newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
            # newZip.close()

            # TODO Walk the entire folder tree and compress the files in each folder
            for foldername, subfolders, filenames in os.walk(folder):
                # add to zip
                print('i am currently in ' + foldername)
                newZip.write(foldername)
                for filename in filenames:
                    if filename.endswith('.zip'):
                        continue
                    newZip.write(os.path.join(foldername, filename))
            print('Done')
            newZip.close()
        else:
            print("no folder selected")
    except Exception as e:
        print("Error:", e)
