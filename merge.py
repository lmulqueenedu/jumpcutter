import os, subprocess
from shutil import rmtree
from time import time
from start import execute, createPath, deletePath

def main():
    TOTALVIDS = int(input("How many videos are you jumpcutting? "))

    FILENAMEL = dict()
    FILENAMER = dict()
    FILENAMEOUT = dict()

    for i in range(TOTALVIDS):
        print("File Number: "+str(i+1))
        FILENAMEL[i] = input("Enter the filepath of the left video: ")
        FILENAMER[i] = input("Enter the filepath of the right video: ")
        FILENAMEOUT[i] = input("What would you like the output file to be called? (Eg. Lecture, Jumpcut): ")

    TEMP_FOLDER = "JCTEMP" + str(int(time()))
    createPath(TEMP_FOLDER)

    for i in range(TOTALVIDS):
        execute("ffmpeg -i "+FILENAMEL[i]+" -i "+FILENAMER[i]+" -filter_complex hstack "+TEMP_FOLDER+"/"+FILENAMEOUT[i]+"_merge.mp4")
        execute("py jumpcutter.py --input_file "+TEMP_FOLDER+"/"+FILENAMEOUT[i]+"_merge.mp4 --output_file Output/"+FILENAMEOUT[i]+"_jumpcut.mp4 --sounded_speed 1.6 --silent_speed 999999 --frame_margin 4")

    deletePath(TEMP_FOLDER)

    print("All done!")
    input("Press ENTER to exit.")

if __name__ == "__main__":
    main()
