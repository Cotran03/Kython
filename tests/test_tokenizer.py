# Imports
from tokenizer import tokenize

# Example
source_code = """ """

# Run Tokenizer
tokens = tokenize(source_code)
for token in tokens:
  print(token)