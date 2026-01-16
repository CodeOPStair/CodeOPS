CodeOPS

CodeOPS is an operations-oriented programming language focused on automation
and task execution.

The goal of CodeOPS is to reduce boilerplate and make scripts readable,
direct and action-driven.

Everything is an operation.

Features

* Simple syntax
* Operations with op { }
* Variable definitions
* Shell command execution
* Variable substitution inside commands

Example

set app = "CodeOPS"

op start {
run "echo Running ${app}"
}

start()

How to run

python cli/codeops.py examples/hello.ops

Project structure

core/       language engine (lexer, parser, executor)
cli/        command line interface
examples/   example scripts
tests/      test scripts
docs/       documentation

Status

Early prototype.
Breaking changes are expected.

License

See LICENSE file.
