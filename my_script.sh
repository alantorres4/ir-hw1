#!/bin/bash


python3 extract_tokens.py test_files output_directory


cd output_directory;
cat * >alltokens
ls
sort alltokens >alltokens.sorted
uniq alltokens.sorted >alltokens.sortedToken -c
sort -nr alltokens.sortedToken >alltokens.sortedFrequency

rm alltokens
rm alltokens.sorted


cd ..
python3 my_nltk_script.py test_files nltk_output


cd nltk_output;
cat * >alltokens
ls
sort alltokens >alltokens.sorted
uniq alltokens.sorted >alltokens.sortedToken -c
sort -nr alltokens.sortedToken >alltokens.sortedFrequency

rm alltokens
rm alltokens.sorted

exit