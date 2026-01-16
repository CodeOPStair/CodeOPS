import sys
from core.lexer import tokenize
from core.parser import parse
from core.executor import execute

def main():
if len(sys.argv) < 2:
print("CodeOPS usage:")
print("  codeops <file.ops>")
sys.exit(1)

```
file_path = sys.argv[1]

if not file_path.endswith(".ops"):
    print("Error: CodeOPS files must end with .ops")
    sys.exit(1)

try:
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
except FileNotFoundError:
    print("Error: file not found:", file_path)
    sys.exit(1)

try:
    tokens = tokenize(code)
    ast = parse(tokens)
    execute(ast)
except Exception as e:
    print("CodeOPS Runtime Error:")
    print(e)
    sys.exit(1)
```

if **name** == "**main**":
main()
