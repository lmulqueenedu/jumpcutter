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

# actual program
TOTALVIDS = int(input("How many videos are you jumpcutting? "))

FILENAME = dict()
FILENAMEOUT = dict()

for i in range(TOTALVIDS):
    print("File Number: "+str(i+1))
    FILENAME[i] = input("Enter the filepath of the video: ")
    FILENAMEOUT[i] = os.path.splitext(os.path.basename(FILENAME[i]))[0]

#TEMP_FOLDER = "JCTEMP" + str(int(time()))
#createPath(TEMP_FOLDER)

for i in range(TOTALVIDS):
	execute("py jumpcutter.py --input_file "+FILENAME[i]+" --output_file Output/"+FILENAMEOUT[i]+".mp4 --sounded_speed 1.6 --silent_speed 999999 --frame_margin 4")

print("All done!")
input("Press ENTER to exit.")
