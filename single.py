import os, subprocess
from shutil import rmtree
from time import time
from start import execute, createPath, deletePath

def main():
    TOTALVIDS = int(input("How many videos are you jumpcutting? "))

    FILENAME = dict()
    FILENAMEOUT = dict()

    for i in range(TOTALVIDS):
        print("File Number: "+str(i+1))
        FILENAME[i] = input("Enter the filepath of the video: ")
        FILENAMEOUT[i] = os.path.splitext(os.path.basename(FILENAME[i]))[0]

    for i in range(TOTALVIDS):
    	execute("py jumpcutter.py --input_file "+FILENAME[i]+" --output_file Output/"+FILENAMEOUT[i]+"_jumpcut.mp4 --sounded_speed 1.6 --silent_speed 999999 --frame_margin 4")

    print("All done!")
    input("Press ENTER to exit.")

if __name__ == "__main__":
    main()
