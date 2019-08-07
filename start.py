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


#file should be located in the 'input' folder
FILENAME = input("What is the file's name?")
TEMP_FOLDER = "SEGTEMP" + str(int(time()))

#Create temporary directories
createPath(TEMP_FOLDER)
createPath(TEMP_FOLDER+"/parts")
createPath(TEMP_FOLDER+"/jcparts")

execute("ffmpeg -i input/"+FILENAME+"_s1.mp4 -i input/"+FILENAME+"_s2.mp4 -filter_complex hstack "+TEMP_FOLDER+"/"+FILENAME+"_stitched.mp4")
execute("ffmpeg -i "+TEMP_FOLDER+"/"+FILENAME+"_stitched.mp4 -c copy -map 0 -segment_time 00:20:00 -f segment -reset_timestamps 1 "+TEMP_FOLDER+"/parts/"+FILENAME+"_stitched_%03d.mp4")

for file in os.listdir(TEMP_FOLDER+"/parts"):
    execute("py jumpcutter.py --input_file "+TEMP_FOLDER+"/parts/"+file+" --output_file "+TEMP_FOLDER+"/jcparts/"+file+" --sounded_speed 1.5 --silent_speed 8 --frame_margin 2")

with open(TEMP_FOLDER+"/list.txt", "w") as a:
    for file in os.listdir(TEMP_FOLDER+"/jcparts"):
        a.write("file '"+"jcparts/"+file+"'\n")

execute("ffmpeg -f concat -safe 0 -i "+TEMP_FOLDER+"/list.txt -c copy "+FILENAME+"_jumpcut.mp4")

#Delete temporary directory
deletePath(TEMP_FOLDER)
