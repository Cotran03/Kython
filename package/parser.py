class Parser:
  def __init__(self, tokens):
    self.tokens = tokens
    self.position = 0

  def current_token(self):
    return self.tokens[self.position] if self.position < len(self.tokens) else None

  def advance(self):
    while self.current_token() and self.current_token()[0] == 'WHITESPACE':
      self.position += 1
    self.position += 1

  def match(self, token_type):
    token = self.current_token()
    if token and token[0] == token_type:
      self.advance()
      return token
    return None

  def parse_function(self):
    if self.match("KEYWORD") and self.current_token()[1] == "함수":
      self.advance()
      name = self.match("IDENTIFIER")
      self.match("PARENTHESIS")
      params = []
      while self.current_token() and self.current_token()[0] != "PARENTHESIS":
        params.append(self.match("IDENTIFIER"))
        self.match("COMMA")
      self.match("PARENTHESIS")
      self.match("COLON")
      body = self.parse_block()
      return {"type": "FunctionDef", "name": name[1], "parameters": [p[1] for p in params], "body": body}

  def parse_block(self):
    block = []
    while self.current_token() and self.current_token()[0] != "DEDENT":
      statement = self.parse_statement()
      if statement:
        block.append(statement)
    return block

  def parse_statement(self):
    if self.match("KEYWORD") and self.current_token()[1] == "반환":
      self.advance()
      expr = self.parse_expression()
      return {"type": "Return", "value": expr}
    return None

  def parse_expression(self):
    token = self.match("NUMBER") or self.match("IDENTIFIER")
    return {"type": "Literal", "value": token[1]} if token else None
