#!/usr/bin/python3
from sympy import *

z, p = symbols("z p")

def expected(pgf):
    return simplify(pgf.diff(z).subs({z:1}))

def var(pgf):
    return simplify(pgf.diff(z, z).subs({z:1}) + pgf.diff(z).subs({z:1}) - (pgf.diff(z).subs({z:1}))**2)

if __name__ == "__main__":
    pgf = parse_expr(input("Please input the pgf with z as the variable\n"))
    print("Expected value:")
    pprint(expected(pgf))

    print("Variance:")
    pprint(var(pgf))