#!/usr/bin/env python3
"""Berechnet Dinge."""

from argparse import ArgumentParser


def op_add(a: int, b: int) -> int:
    """Addiert a und b."""
    return a + b


def op_sub(a: int, b: int) -> int:
    """Subtrahiert b von a."""
    return a - b


def op_mult(a: int, b: int) -> int:
    """Multipliziert a mit b."""
    return a * b


def op_div(a: int, b: int) -> float:
    """Teilt a durch b."""
    return a / b


def op_exp(a: int, b: int) -> int:
    """Potenziert a mit b."""
    return a ** b


def op_root(a: int, b: int) -> float:
    """Berechnet die a-te Wurzel von b."""
    return b ** (1 / a)


parser = ArgumentParser(description=__doc__)
subparsers = parser.add_subparsers(
    dest="command",
    help="die auszuführende Rechenoperation"
)
subparsers.required = True

for function in (
    op_add,
    op_sub,
    op_mult,
    op_div,
    op_exp,
    op_root,
):
    parser_func = subparsers.add_parser(
        function.__name__.lstrip("op_"),
        help=function.__doc__
    )
    parser_func.add_argument("a", help="erster Wert", type=int)
    parser_func.add_argument("b", help="zweiter Wert", type=int)
    parser_func.set_defaults(func=function)

if __name__ == "__main__":
    # Verarbeiten der Argumente
    args = parser.parse_args()
    # die tatsächliche Funktion aufrufen
    res = args.func(args.a, args.b)
    print(res)
