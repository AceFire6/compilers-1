import ply.lex as lex
import sys


# List of token names.
tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'EQUALS',
    'FLOAT_LITERAL',
)

if __name__ == '__main__':
    tokens += ('WHITESPACE', 'COMMENT',)

# outputs that don't require a label
unnamed_output = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
)

# Regular expression rules for simple tokens
if __name__ == '__main__':
    t_COMMENT = r'(//.*|/\*([\w\s]|\n)*\*/)'
    t_WHITESPACE = r'\s+'
else:
    t_ignore_COMMENT = r'(//.*|/\*([\w\s]|\n)*\*/)'
    t_ignore_WHITESPACE = r'\s+'

t_PLUS = r'\@'
t_MINUS = r'\$'
t_TIMES = r'\#'
t_DIVIDE = r'\&'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_ID = r'[_a-zA-Z][a-zA-Z0-9]*'
t_FLOAT_LITERAL = r'[-]?(\d*[.eE])?[-]?\d+'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Reads file and gives the lexer it's contents.
# Handle the different output styles.
def lex_file(file_name):
    with open(file_name) as open_file:
        lexer.input(open_file.read())
        while True:
            token = lexer.token()
            if not token:
                break
            if token.type in ('WHITESPACE', 'COMMENT'):
                print token.type
            elif token.type in unnamed_output:
                print token.value
            else:
                print '%s,%s' % (token.type, token.value)

lexer = lex.lex()

if __name__ == '__main__':
    ula_file = sys.argv[-1]
    # Check for argument
    if ula_file == sys.argv[0]:
        print 'No ula file specified!'
    else:
        lex_file(ula_file)

