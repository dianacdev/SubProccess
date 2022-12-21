from subprocess import run
import os
import random

flag_list =[]
flag_name = ""
total_bytes = 0
def open_file(string, list_variable):
    """takes a string/filename turns file into list attached to listVariable."""
    with open(string, "r", encoding='utf-8') as file:
        file = file.readlines()
        for line in file:
            list_variable.append(line.strip())

open_file("flags.txt", flag_list)
for i in range(10):
    flag_name = random.choice(flag_list)
    run(f"curl https://www.sciencekids.co.nz/images/pictures/flags680/{flag_name}.jpg -o {flag_name}.jpg", shell=True)
    total_bytes += (os.stat(flag_name +".jpg")).st_size
print(f"Total bytes downloaded: {total_bytes}")