# Imports
from tokenizer import tokenize
from parser import Parser

# Example
source_code = """ """

# Run Tokenizer
tokens = tokenize(source_code)

# Run Parser
parser = Parser(tokens)
ast = parser.parse_function()

# Print
print('\nAST: ')
print(ast)
