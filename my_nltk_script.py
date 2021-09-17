import os

import nltk
import shutil
import sys
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

input_files = sys.argv[1]
output_directory = os.path.join(os.getcwd(), sys.argv[2])

if(os.path.exists(output_directory)):
    shutil.rmtree(output_directory)

os.mkdir(output_directory)

directory = os.getcwd()
count = 0
for filename in os.listdir(directory+'/'+input_files):
    count = count +1 #just making a count so it only read "simple.html" for now, will remove count later
    if count > 1:
      break
    print("filename: ",filename)
    readFile = open(directory+'/'+input_files+'/'+filename, "r")
    result = readFile.read()
    tokenized_result = word_tokenize(result)
    
    # --section where we put all the final tokens into a next txt file line by line
    resultFile = open("nltk_output_"+filename+".txt", "w")
    for token in tokenized_result:
        resultFile.write(token+'\n')
    resultFile.close()


#experimenting with parsing out some html... kind of stuck
tokenizer = RegexpTokenizer(r"\w+")  #so this will take out the punctuation and "<" or ">" parts of the html
lst=tokenizer.tokenize(result)       # I just cant figure out how to get rid of head from <head> etc.
print(' '.join(lst))


    
