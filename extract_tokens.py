# NOT FINISHED
# to run:
# python3 extract_tokens.py files output_directory
import sys
import os
import shutil
import ply
from ply import lex
from ply.lex import TOKEN

# LIST OF TOKENS
tokens =[
'htmltag',
'lowercase',
'whitespace',
'digit',
'other'
]

# SECTION OF CODE WHICH SPECIFIES LEX SUBSTITUTION PATTERNS
DIGITS = r'[0-9]+'
UPPERCASE = r'[A-Z]'

# TOKENS DEFINITION - SECTION WHICH SPECIFIES REGULAR EXPRESSIONS AND ACTION
#def t_whitespace(t):
# r''
# pass

def t_htmltag(t):
    r'<.*?>'
    t.value = ''
    return t

def t_other(t):
    r'[a-z]+'
    return t

# // In some applications, we may want to define tokens as a series of more complex regular expression rules.
@TOKEN(DIGITS)
def t_digit(t):
    t.value = "NUMBER"
    return t

@TOKEN(UPPERCASE)
def t_lowercase(t):
    t.value = t.value[0].lower()
    return t

def t_error(t):
    t.lexer.skip(1)


# READING INPUT FILE
directory = sys.argv[1] # input directory from command line
output_directory = os.path.join(os.getcwd(), sys.argv[2]) # output directory from command line

if(os.path.exists(output_directory)):
    # maybe remove this directory and all its contents and mkdir() immediately after?
    pass 
else:
    os.mkdir(output_directory)

input_files = os.listdir(directory)
# For each file in the input_directory, tokenize & downcase, then output all of that into a new file. 
# Then add that output file into a new directory.
for file in input_files:
    # --------------------------------------------
    inputFile = open(os.getcwd()+"/"+directory+"/"+file, "r")
    result = ""
    lexer = lex.lex()

    with inputFile as fp:
        for line in fp:
            try:
                lexer.input(line)
                for token in lexer:
                    result = result + token.value + '\n'
            except EOFError:
                break

    # print(result)
    # 'result' now holds the entire tokenized inputFile
    # Make a new file, output to it.
    outputFile_name = file + "_tokenized.txt"
    outputFile = open(outputFile_name, "w")
    outputFile.write(result)
    # Then move() that file to the new output_directory
    shutil.move(os.getcwd()+"/"+outputFile_name, output_directory)
    # --------------------------------------------
