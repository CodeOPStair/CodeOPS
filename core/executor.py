import subprocess

variables = {}
operations = {}

def execute(ast):
# Primera pasada: registrar operaciones
for node in ast:
if node["type"] == "op":
operations[node["name"]] = node["body"]

```
# Segunda pasada: ejecutar instrucciones
for node in ast:
    if node["type"] == "set":
        variables[node["name"]] = node["value"]

    elif node["type"] == "run":
        run_command(node["command"])

    elif node["type"] == "op":
        pass  # las ops no se ejecutan solas

    elif node["type"] == "call":
        call_operation(node["name"])
```

def run_command(command):
# Reemplazo simple de variables: ${var}
for key, value in variables.items():
command = command.replace("${" + key + "}", value)

```
print("[CodeOPS] running:", command)
subprocess.run(command, shell=True)
```

def call_operation(name):
if name not in operations:
raise RuntimeError("Operation not found: " + name)

```
for instruction in operations[name]:
    if instruction["type"] == "run":
        run_command(instruction["command"])
```
