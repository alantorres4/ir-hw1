import os
import sys
import nltk
#test in dev-josh

# inputFile = input("Enter a .html file to read: ")
# outputFile = input("Name a file for the parsed txt to live in: ")


# #f = open(inputFile, "r")
# #print(f.read())

# with open(inputFile, mode='r') as in_file, \
#      open(outputFile, mode='w') as out_file:

#     # A file is iterable
#     # We can read each line with a simple for loop
#     for line in in_file:
#         for word in line.split():
#             out_file.write(word)
#             out_file.write("\n")
# f = open(outputFile, mode="r")
# print("reading outputFile ",outputFile, "\n", f.read())


directory = input("input name of directory: ")
file = input("input name of file within directory: ")
print(os.listdir(directory))
f = open(os.getcwd()+"/"+directory+"/"+file, "r")
print(f.read())
print("CWD: ",os.getcwd())
print('done')