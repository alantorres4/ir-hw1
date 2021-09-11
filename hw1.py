import os
import sys
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

print("CWD: ",os.getcwd())

directory = input("input name of directory('files'): ")
file = input("input name of file within directory('simple.html'): ")

f = open(os.getcwd()+"/"+directory+"/"+file, "r")
readFile = f.read()


parsedFile = word_tokenize(readFile)
print("parsedFile ",parsedFile)
print('done')