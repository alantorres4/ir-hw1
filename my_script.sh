#!/bin/bash


python3 extract_tokens.py files output_directory


cd output_directory;
cat * >alltokens
ls
sort alltokens >alltokens.sorted
uniq alltokens.sorted >alltokens.sortedToken -c
sort alltokens.sortedToken >alltokens.sortedFrequency

rm alltokens
rm alltokens.sorted

exit