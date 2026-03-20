from lexer import Lexer, Token, TokenType
from dataclasses import dataclass
from ast_nodes import *

@dataclass
class Parser:
	tokens: list
	pos: int = 0

	def peek(self):
		if self.pos < len(self.tokens):
			return self.tokens[self.pos]
		else:
			return None

	def advance(self):
		if self.pos < len(self.tokens):
			char = self.tokens[self.pos]
			self.pos += 1
			return char
		else:
			return None

	def parse(self):
		nodes = []

		while self.peek().type != TokenType.EOF:
			char = self.peek()
			if char.type == TokenType.NEWLINE:
				self.advance()
			elif char.type == TokenType.IDENT and char.value == "module":
				self.advance()
				kind = self.advance().value
				body = []
				while self.peek() is not None and not (self.peek().type == TokenType.IDENT and self.peek().value == "module") and self.peek().type != TokenType.EOF:
				    # parse whatever is inside and append to body
				    self.advance()
				nodes.append(ModuleNode(kind, body))
			else:
				self.advance()
		return nodes

if __name__ == "__main__":
    with open("source.s64") as f:
        src = f.read()
    lexer = Lexer(src)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)