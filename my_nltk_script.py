import os
import re
import shutil
import sys
from nltk.tokenize import word_tokenize
import time

#starting time
start = time.time()





input_files = sys.argv[1]
output_directory = os.path.join(os.getcwd(), sys.argv[2])

if(os.path.exists(output_directory)):
    shutil.rmtree(output_directory)

os.mkdir(output_directory)

directory = os.getcwd()
punc = '''!()-[]{};:'"\,<>''./?@#```$%^&*_~'''

for filename in os.listdir(directory+'/'+input_files):
    readFile = open(directory+'/'+input_files+'/'+filename, "r")
    result = readFile.read()
    removedHtml_result = re.sub(r"<.*?>", "", result) # removes all the HTML tags
    tokenized_result = word_tokenize(removedHtml_result)
    
    # --section where we put all the final tokens into a next txt file line by line
    resultFile = open("nltk_output_"+filename+".txt", "w")
    for token in tokenized_result:
        if token not in punc:
                resultFile.write(token.lower()+'\n')
    shutil.move(resultFile.name, output_directory)
    resultFile.close()


# end time
end = time.time()

# total time taken
print("Execution time for nltk code with 3 is- ", end-start)
