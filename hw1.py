# This is just a test file.
# This is the basics of creating directories, reading, etc.
# Need to transfer the ideas from this file to complete the extract_tokens.py file

import os
import shutil
import sys

directory = input("input name of directory: ")
output_directory = os.path.join(os.getcwd(), "output_directory")

if(os.path.exists(output_directory)):
    # maybe remove this directory and all its contents and mkdir() immediately after?
    pass 
else:
    os.mkir(output_directory)

# GO THROUGH, OPEN EACH FILE, TOKENIZE AND DOWNCASE, AND THEN OUTPUT TO A NEW DIRECTORY
input_files = os.listdir(directory)
for file in input_files:
    print(f"file = {file}")
    print("-------------------------------")
    f = open(os.getcwd()+"/"+directory+"/"+file, "r")
    print(f.read())
    # TOKENIZE AND DOWNCASE HERE
    # THEN SEND THAT NEW FILE TO THE NEW DIRECTORY
    shutil.copy(os.getcwd()+"/"+directory+"/"+file, output_directory+"/")

print("CWD: ",os.getcwd())

# Read in: directory name for the input documents from command line
# Read in: directory name for the output documents from the command line

# Program should produce 3 things:
#   1. Directory of all tokenized documents (one putput file per input file) ()
#   2. A file of ALL tokens and their frequencies sorted by token ()
#   3. A file of ALL tokens and their frequencies sorted by frequency

# I can use the UNIX sort facility to sort the output files. However, there must be a single command line call:
#   $ tokenize input-directory output-directory

# PAIRS:
#   EXTRA: Implement the tokenization using an existing tokenizer (NLTK)
#   This separate program should also create the same 3 things with this approach.