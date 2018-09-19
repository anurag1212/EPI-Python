from test_framework import generic_test


def evaluate_this(A, B, op):
    ops = ['+', '-', '*', '/']
    if type(A) == str: A = eval(A)
    if type(B) == str: B = eval(B)
    if op == ops[0]:
        return A + B
    elif op == ops[1]:
        return A - B
    elif op == ops[2]:
        return A * B
    elif op == ops[3]:
        return A // B


def isnumeric(data):
    return type(data) == int or data.isdigit() or data[1:].isdigit()


def evaluate(expression):
    expression = expression.split(',')
    stk = [expression[-1]]
    ptr = len(expression) - 2
    while not isnumeric(stk[0]):
        l = stk.pop()
        if stk and isnumeric(stk[-1]) and isnumeric(l):
            r = stk.pop()
            op = stk.pop()
            stk.append(evaluate_this(l, r, op))
        else:
            stk.append(l)
            if ptr >= 0:
                stk.append(expression[ptr])
                ptr -= 1
    return eval(stk[0]) if type(stk[0]) == str else stk[0]


def evaluate_recursive(expression):
    expression = expression.split(',')
    pointer = [len(expression)-1]

    def rpn():
        val = expression[pointer[0]]
        if isnumeric(val): return eval(val)
        pointer[0] -= 1
        R = rpn()
        pointer[0] -= 1
        L = rpn()
        return evaluate_this(L, R, val)

    return rpn()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
