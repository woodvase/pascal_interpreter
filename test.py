from token import Token
from ast import Num, BinOp
from visitor import Interpreter

INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF'

mul_token = Token(MUL, '*')
plus_token = Token(PLUS, '+')
mul_node = BinOp(
    left=Num(Token(INTEGER, 2)),
    op=mul_token,
    right=Num(Token(INTEGER, 7))
)

add_node = BinOp(
    left=mul_node,
    op=plus_token,
    right=Num(Token(INTEGER, 3))
)

inter = Interpreter(None)
print(inter.visit(add_node))