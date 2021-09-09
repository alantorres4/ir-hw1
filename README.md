# ir-hw1
Information Retrieval -- Homework 1

PROJECT DETAILS

The objective of this assignment is to tokenize and downcase all words in a collection of HTML documents. You may choose any of the following approaches: flex, javacc, other publicly available tokenizer, or custom code in C, C++, Python, or Java. You must write your own rules for tokenization, removal of HTML tags, downcaseing, etc. Each program should read a directory name for the input documents from the command line and a directory name for the output documents from the command line. It should produce 3 things
a directory of all tokenized documents (one output file per input file) 
a file of all tokens and their frequencies sorted by token 
a file of all tokens and their frequencies sorted by frequency
You may use the UNIX sort facility to sort the output files. However, there must be a single command line call to your function, e.g., 
turing$ tokenize input-dir output-dir
>Pairs If you work in pairs, you should also implement the tokenization using an existing tokenizer, e.g., NLTK, JSoup, BeautifulSoup, etc. You should create the same 3 things with this approach.

Program Testing 
There are a set of files to be preprocessed in /home/sgauch/public_html/5533/files/ on turing. For initial testing, copy a few of these files into your home directory for processing. If you want a copy, you can get the copy the whole batch into your turing directory with:
cp /home/sgauch/public_html/5533/files.tar .
or onto your personal computer with using the following url: files.tar

Program Documentation. 
After your internal documentation (comments) is complete, write a report that provides a short executive summary of your programs. There is a sample report template posted online. Include timings and the tokens created from simple.html, medium.html, hard.html, and 990.html

how you handled punctuation and numbers 
describe how you calculated the frequency of each word 
identify some words which are incorrectly tokenized (if any) and discuss why your program does not handle them properly 
discuss the efficiency of your tokenization program in terms of order of magnitude 
Include a small graph or table of time versus number of documents processed
The entire document should be 5 pages maximum (7 pages for pairs). I will primarily be grading from the report, so make sure it clearly describes what you did, your program's output, performance (runtimes), and computational efficiency (analysis your approach's big-O complexity).
If you work in pairs

You must implement one version using a lex variation (Flex, JFlex, or Ply) and one using a tokenization package. Your report should discuss the differences between the resulting tokens and the differences in the efficiency of the two versions of the solution in terms of runtime and also the number and types of tokens each approach used. If you cannot install the package on turing, you may submit 2 timing charts: 1 that compares the two approaches showing timings on the same computer (any computer) and another that shows the lex approach running on turing.
Hand In 
Upload your report and code to Blackboard. Only one person in a pair needs to upload the code and report. The other partner should just upload a note saying "Partnered with X who submitted the code and report.". The report should clearly indicate both names in the partnership. 

Late Policy 
10% deduction per 24 hours for a maximum of 3 days.