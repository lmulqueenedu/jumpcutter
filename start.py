import sys, subprocess

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

def main():
    print("Welcome to the lecture jumpcutter!")
    print("Do you need to merge 2 videos together? Useful for some Math lectures. [Y/N]")
    usr_input = input()
    while usr_input not in ['Y', 'N', 'y', 'n']:
        usr_input = input("Please type either Y or N, then press ENTER to confirm: ")

    if usr_input in ['N', 'n']:
        execute("py single.py")
    elif usr_inputin ['Y', 'y']:
        execute("py merge.py")

    sys.exit()

if __name__ == "__main__":
    main()
