import sys
import ply.yacc as yacc

import lex_ula

tokens = lex_ula.tokens


def p_program(p):
    """program : program assign"""
    p[0] = p[1] + (p[2],)


def p_program_assign(p):
    """program : assign"""
    p[0] = ('Program', p[1])


def p_assign_expr(p):
    """assign : ID EQUALS expr"""
    p[0] = ('AssignStatement', ('ID,%s' % p[1], p[3]))


def p_expr_plus(p):
    """expr : term PLUS term
            | expr PLUS term"""
    p[0] = ('AddExpression', p[1], p[3])


def p_expr_minus(p):
    """expr : term MINUS term
            | expr MINUS term"""
    p[0] = ('SubExpression', p[1], p[3])


def p_term_mul(p):
    """term : term TIMES term"""
    p[0] = ('MulExpression', p[1], p[3])


def p_term_div(p):
    """term : term DIVIDE term"""
    p[0] = ('DivExpression', p[1], p[3])


def p_expr_term(p):
    """expr : term"""
    p[0] = p[1]


def p_term_factor(p):
    """term : factor"""
    p[0] = p[1]


def p_factor_id(p):
    """factor : ID"""
    p[0] = ('IdentifierExpression', ('ID,%s' % p[1],))


def p_factor(p):
    """factor : FLOAT_LITERAL"""
    p[0] = ('FloatExpression', ('FLOAT_LITERAL,%s' % p[1],))


def p_factor_expr(p):
    """factor : LPAREN expr RPAREN"""
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)
    exit()


# Recursively prints the AST
def print_ast(ast, file_handle, depth):
    tabs = '\t' * depth
    for branch in ast:
        if type(branch) == str:
            if 'ID,' in branch:
                depth -= 1
            file_handle.write(tabs + branch + '\n')
            print(tabs + branch)
        else:
            print_ast(branch, file_handle, depth+1)

if __name__ == '__main__':
    # Build the parser
    parser = yacc.yacc()

    ula_file = sys.argv[-1]
    # Check for argument
    if ula_file == sys.argv[0]:
        print('No ula file specified!')
    else:
        with open(ula_file) as open_file:
            in_data = open_file.read()

        parsed_ula = parser.parse(in_data)
        with open(ula_file.replace('.ula', '.ast'), 'w') as out_file:
            print('Start')
            out_file.write('Start\n')
            print_ast(parsed_ula, out_file, 1)
