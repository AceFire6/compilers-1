import sys
import ply.yacc as yacc

import lex_ula

tokens = [token for token in lex_ula.tokens
          if token not in ('COMMENT', 'WHITESPACE',)]


def p_assign_expr(p):
    """assign : ID EQUALS expr
              | ID EQUALS factor"""
    p[0] = ('AssignStatement', ('ID,%s' % p[1], p[3]))


def p_expr_plus(p):
    """expr : term PLUS term"""
    p[0] = ('AddExpression', p[1], p[3])


def p_expr_minus(p):
    """expr : term MINUS term"""
    p[0] = ('SubExpression', p[1], p[3])


def p_term_mul(p):
    """term : term TIMES factor"""
    p[0] = ('MulExpression', p[1], p[3])


def p_term_div(p):
    """term : term DIVIDE factor"""
    p[0] = ('DivExpression', p[1], p[3])


def p_term_factor(p):
    """term : factor"""
    p[0] = p[1]


def p_factor(p):
    """factor : FLOAT_LITERAL"""
    p[0] = 'FloatExpression', ('FLOAT_LITERAL,%s' % p[1],)


def p_factor_expr(p):
    """factor : LPAREN expr RPAREN"""
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!", p


def print_ast(ast, depth):
    if depth == 0:
        print('Start')
        print('\tProgram')
        depth += 2
        print_ast(ast, depth)
    else:
        tabs = '\t' * depth
        for branch in ast:
            if type(branch) == str:
                print(tabs + branch)
            else:
                print_ast(branch, depth+1)

if __name__ == '__main__':
    # Build the parser
    parser = yacc.yacc()

    ula_file = sys.argv[-1]
    # Check for argument
    if ula_file == sys.argv[0]:
        print 'No ula file specified!'
    else:
        s = 'result = 12#(60$2e4)'.replace(' ', '')
        a = parser.parse(s)
        print a
        print_ast(a, 0)
