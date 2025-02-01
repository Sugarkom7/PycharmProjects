"""
import os
new_file = open("secret_files.txt","w+")
new_file.write("Hello God!")
print(new_file.read())
new_file.close()
os.rename("secret_files.txt", "shared_files.txt")
#os.remove("secret_files.txt")  to delete a file
"""
import sys
randomlist = ["a", 0, 2]
for entry in randomlist:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
        break
    except:
        print("oops! Error")
        print("Next entry")
        print()
print("The reciprocal of the", entry, r)



