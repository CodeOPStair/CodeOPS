def parse(tokens):
ast = []
i = 0

```
def current():
    return tokens[i] if i < len(tokens) else None

while i < len(tokens):
    token = current()

    if token["type"] == "SET":
        name = tokens[i + 1]["value"]
        value = tokens[i + 3]["value"]
        ast.append({
            "type": "set",
            "name": name,
            "value": value.strip('"')
        })
        i += 4

    elif token["type"] == "RUN":
        command = tokens[i + 1]["value"].strip('"')
        ast.append({
            "type": "run",
            "command": command
        })
        i += 2

    elif token["type"] == "OP":
        op_name = tokens[i + 1]["value"]
        i += 3  # salta: OP name {

        body = []
        while tokens[i]["type"] != "RBRACE":
            if tokens[i]["type"] == "RUN":
                cmd = tokens[i + 1]["value"].strip('"')
                body.append({
                    "type": "run",
                    "command": cmd
                })
                i += 2
            else:
                i += 1

        ast.append({
            "type": "op",
            "name": op_name,
            "body": body
        })
        i += 1  # salta }

    else:
        i += 1

return ast
```
