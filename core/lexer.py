import re

TOKEN_REGEX = [
("SET", r"\bset\b"),
("OP", r"\bop\b"),
("RUN", r"\brun\b"),
("IF", r"\bif\b"),
("ELSE", r"\belse\b"),
("IDENT", r"[a-zA-Z_][a-zA-Z0-9_]*"),
("STRING", r'"[^"]*"'),
("NUMBER", r"\d+"),
("LBRACE", r"{"),
("RBRACE", r"}"),
("LPAREN", r"("),
("RPAREN", r")"),
("EQUALS", r"="),
("ARROW", r"->"),
("NEWLINE", r"\n"),
("SKIP", r"[ \t]+"),
]

def tokenize(code):
tokens = []
line = 1

```
while code:
    match = None

    for token_type, regex in TOKEN_REGEX:
        pattern = re.compile(regex)
        match = pattern.match(code)

        if match:
            text = match.group(0)

            if token_type == "NEWLINE":
                line += 1
            elif token_type != "SKIP":
                tokens.append({
                    "type": token_type,
                    "value": text,
                    "line": line
                })

            code = code[len(text):]
            break

    if not match:
        raise SyntaxError(
            f"CodeOPS Lexer Error | line {line} | unknown token near: {code[:10]}"
        )

return tokens
```
