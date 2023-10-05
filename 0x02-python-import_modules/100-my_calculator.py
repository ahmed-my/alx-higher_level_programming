#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys
    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = {"+": add, "-": sub, "*": mul, "/": div}
    operator_symbol = sys.argv[2]

    if operator_symbol not in operator:
        print("Unknown operator. Available operations: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    result = operator[operator_symbol](a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, result))
