import os
import time
import shutil
import logging

curDir = "/home/suraj/Downloads/"
files_to_delete = []
# The important file extensions to avoid accidental deletions
Important_files_extensions = ('.py', '.png', '.txt', '.pdf', '.jpg', '.doc')
# Delete files older than 1 week when the script executes
Delete_After = 24*7

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='/home/suraj/file_cleaning.log',level=logging.INFO)

# Checking for files older than a week
def check_old_files(file):
    return time.time() - os.path.getmtime(curDir+file) > (3600 * Delete_After)

# Recursively spanning the curdir and checking files for various conditionals
for files in os.listdir(curDir):
    name, ext = os.path.splitext(files)
    if files.startswith('.'):
        pass
    elif ext in Important_files_extensions:
        pass
    elif check_old_files(files):
        files_to_delete.append(curDir+files)


# Now recursively delete files from the files_to_delete list we acquired
for bad_files in files_to_delete:
    if os.path.isdir(bad_files):
        try:
            shutil.rmtree(bad_files)
            logging.info("The directory "+bad_files+" was deleted")
        except PermissionError:
            logging.info("The directory " + bad_files + " was could not be deleted dut to bad permissions")
    else:
        try:
            os.remove(bad_files)
            logging.info("The file " + bad_files + " was deleted")
        except PermissionError:
            logging.info("The directory " + bad_files + " was could not be deleted dut to bad permissions")
