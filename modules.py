import os

def dirCD():
# Get the current working directory.
    current_directory = os.getcwd()

    # Create a list of all the files in the current directory.
    files = os.listdir(current_directory)

    # Print the list of files.
    print("The following files are in the current directory:")
    for file in files:
        print(file)