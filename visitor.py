class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
            raise Exception('Method visit_{} not found'.format(type(node).__name__))

class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_Num(sefl, node):
        return node.value

    def visit_BinOp(self, node):
        type = node.op.type
        match type:
            case 'PLUS':
                return self.visit(node.left) + self.visit(node.right)
            case 'MINUS':
                return self.visit(node.left) - self.visit(node.right)
            case 'MUL':
                return self.visit(node.left) * self.visit(node.right)
            case 'DIV':
                return self.visit(node.left) / self.visit(node.right)
    
    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

