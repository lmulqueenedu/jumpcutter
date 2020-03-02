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
