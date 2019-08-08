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

FILENAMEL = dict()
FILENAMER = dict()
FILENAMEOUT = dict()

for i in range(TOTALVIDS):
    print("File Number: "+str(i+1))
    FILENAMEL[i] = input("Enter the filepath of the left file: ")
    FILENAMER[i] = input("Enter the filepath of the right file: ")
    FILENAMEOUT[i] = input("What would you like the output file to be called? (Eg. Lecture, Jumpcut) ")
    print()

for i in range(TOTALVIDS):
    #Create temporary directories
	TEMP_FOLDER = "SEGTEMP" + str(int(time()))
	createPath(TEMP_FOLDER)
	createPath(TEMP_FOLDER+"/parts")
	createPath(TEMP_FOLDER+"/jcparts")
	
	execute("ffmpeg -i "+FILENAMEL[i]+" -i "+FILENAMER[i]+" -filter_complex hstack "+TEMP_FOLDER+"/"+FILENAMEOUT[i]+"_stitched.mp4")
	execute("py jumpcutter.py --input_file "+TEMP_FOLDER+"/"+FILENAMEOUT[i]+"_stitched.mp4 --output_file "+FILENAMEOUT+".mp4 --sounded_speed 1.6 --silent_speed 999999 --frame_margin 4")
	
	#Delete temporary directory
	deletePath(TEMP_FOLDER)
    

print("All done!")
input("Press ENTER to exit.")
