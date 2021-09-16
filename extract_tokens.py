# NOT FINISHED
# to run:
# python3 extract_tokens.py input.txt > output.txt
import sys
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
# TODO: Right now, this only tokenizes one input file and outputs one file.
# The goal is to have a loop surrounding this so that it tokenized and outputs whole directories of HTML files.
inputFile = open(sys.argv[1])
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

print(result)