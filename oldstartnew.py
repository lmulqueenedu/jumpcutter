import os, subprocess
from shutil import rmtree
from time import time


def execute (cmd):
    subprocess.call(cmd, shell=True)


def createPath(s):

    try:
        os.mkdir(s)
    except OSError:
        assert False, "Creation of the directory %s failed. (The TEMP folder may already exist. Delete or rename it, and try again.)"


def deletePath(s): # Dangerous! Watch out!
    try:
        rmtree(s,ignore_errors=False)
    except OSError:
        print ("Deletion of the directory %s failed" % s)
        print(OSError)

TOTALVIDS = int(input("How many videos are you jumpcutting? "))
print()

FILENAME = dict()
FILENAMEOUT = dict()

for i in range(TOTALVIDS):
    print("File Number: "+str(i+1))
    FILENAME[i] = input("Enter the filepath of the video: ")
    FILENAMEOUT[i] = input("What would you like the output file to be called? (Eg. Lecture, Jumpcut) ")
    print()

TEMP_FOLDER = "JCTEMP" + str(int(time()))
createPath(TEMP_FOLDER)

for i in range(TOTALVIDS):
	execute("py jumpcutter.py --input_file "+FILENAME[i]+" --output_file "+FILENAMEOUT[i]+".mp4 --sounded_speed 1.6 --silent_speed 999999 --frame_margin 4")
   
deletePath(TEMP_FOLDER)

print("All done!")
input("Press ENTER to exit.")
