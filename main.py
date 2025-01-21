# Imports
from package.tokenizer import tokenize
from package.parser import Parser

# Example
source_code = """
함수 더하기(첫번째, 두번째):
  반환 첫번째 + 두번째  # 두 수를 더합니다

# 주석 예제
반지름_값 = 5  # 반지름
결과 = 더하기(반지름_값, 반지름_값 * 2)  # 함수 호출
출력("결과:", 결과)  # 결과 출력

만약 결과 > 10:
  출력("결과가 10보다 큽니다.")
그렇지않으면:
  출력("결과가 10 이하입니다.")
"""

# Run Tokenizer
tokens = tokenize(source_code)
for token in tokens:
  print(token)

# Run Parser
parser = Parser(tokens)
ast = parser.parse_function()

# Print
print('\nAST: ')
print(ast)
