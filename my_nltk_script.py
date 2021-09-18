import os
import re
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
punc = '''!()-[]{};:'"\,<>./?@#`$%^&*_~'''
for filename in os.listdir(directory+'/'+input_files):
    count = count +1 #just making a count so it only read "simple.html" for now, will remove count later
    if count > 3:
      break
    print("filename: ",filename)
    readFile = open(directory+'/'+input_files+'/'+filename, "r")
    result = readFile.read()
    removedHtml_result = re.sub(r"<.*?>", "", result) # removes all the HTML tags
    tokenized_result = word_tokenize(removedHtml_result)
    
    # --section where we put all the final tokens into a next txt file line by line
    resultFile = open("nltk_output_"+filename+".txt", "w")
    print("tokenized_result:",tokenized_result)
    for token in tokenized_result:
        # for ele in token:
        #     if ele in punc:
        #         token = token.replace(ele, " ")
        #         token.split()
        #         print('token:',token)
        #         for elem in token:
        #             resultFile.write(token.lower()+'\n')
        #     else:
        if token not in punc:
                resultFile.write(token.lower()+'\n')
    resultFile.close()


#at this point the file just needs to be cleaned up with the spaces that have replace punc etc.
