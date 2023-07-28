# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination ca  be directory(folder)
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("Copy_a_File_Test.txt", "Copy_a_File_Test2.txt") # source, destination
#                  ^                         ^
#               file copied               new file

# 02/07/23