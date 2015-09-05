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
    'WHITESPACE',
    'COMMENT',
    'ID',
    'EQUALS',
    'FLOAT_LITERAL',
)


class ULALexer(object):
    # List of token names.
    tokens = (
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'WHITESPACE',
        'COMMENT',
        'ID',
        'EQUALS',
        'FLOAT_LITERAL',
    )
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
    t_PLUS = r'\@'
    t_MINUS = r'\$'
    t_TIMES = r'\#'
    t_DIVIDE = r'\&'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_EQUALS = r'='
    t_ID = r'[_a-zA-Z][a-zA-Z0-9]*'
    t_WHITESPACE = r'\s+'
    t_COMMENT = r'(//.*|/\*([\w\s]|\n)*\*/)'
    t_FLOAT_LITERAL = r'[-]?(\d*[.eE])?[-]?\d+'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

    def input(self, data):
        self.lexer.input(data)

    def next_token(self):
        token = self.lexer.token()
        if not token:
            yield None
        yield token

    # Reads file and gives the lexer it's contents.
    # Handle the different output styles.
    def lex(self, file_name):
        with open(file_name) as lex_file:
            self.lexer.input(lex_file.read())
            while True:
                token = self.lexer.token()
                if not token:
                    break
                if token.type in ('WHITESPACE', 'COMMENT'):
                    print token.type
                elif token.type in self.unnamed_output:
                    print token.value
                else:
                    print '%s,%s' % (token.type, token.value)


if __name__ == '__main__':
    ula_file = sys.argv[-1]
    # Check for argument
    if ula_file == sys.argv[0]:
        print 'No ula file specified!'
    else:
        lexer = ULALexer()
        lexer.build()
        lexer.lex(ula_file)

