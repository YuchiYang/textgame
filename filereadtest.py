#!/usr/bin/env python

# Define a filename.
filename = "convo1.txt"

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as f:
    content = f.readlines()

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
i=0
for line in content:
    i+=1
    a=line
    print(a)
    if (a=="HI\n"):
        print("yooooooooooooooooooooooooooooooooooooooooooooooooo")
    print(i,line,end='')
