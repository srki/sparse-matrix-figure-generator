from DrawIo import *


def postfix_to_tree(postfix):
    postfix = postfix.strip()
    tokens = postfix.split(' ')

    operands = []
    for token in tokens:
        if token[0] in ['+', '*', 'x']:
            b = operands.pop()
            a = operands.pop()
            operands.append([token, a, b])
        else:
            operands.append([token])

    assert len(operands) == 1
    return operands[0]


def dimension(expr):
    if len(expr) == 1:
        return 1, 1

    dim = [0, 0]
    for e in expr[1:]:
        d = dimension(e)
        dim[0] = max(dim[0], d[0])
        dim[1] += d[1]

    return dim[0] + 1, dim[1]


class ExprPrint:
    def __init__(self):
        self.lvl = 0
        self.ld = 0
        self.drawio = DrawIo()

    def print_expr(self, expr) -> (int, int):
        if len(expr) == 1:
            self.ld += 1

        self.lvl += 1

        t = [self.print_expr(e) for e in expr[1:]]
        # for e in expr[1:]:
        #     self.print_expr(e)

        if not t:
            pos = self.ld
        else:
            pos = (t[0][0] + t[-1][0]) / 2

        elem_id = self.drawio.add_circle(pos * 60, self.lvl * 60, expr[0])

        if len(t) > 0:
            self.drawio.add_link(elem_id, t[0][1], 0, 1)
            self.drawio.add_link(elem_id, t[-1][1], 1, 1)

        self.lvl -= 1

        return pos, elem_id


def main():
    postfix = 'A0 A1 A2 *2 *2 A3 x A4 A5 A6 +2 A7 A8 *2 *2 *2 +2 A9 A10 A11 A12 +2 *2 *2 A13 x *2 A14 A15 x A16 A17 A18 A19 x +2 +2 A20 x *2 A21 A22 *2 A23 A24 x +2 A25 A26 x A27 *2 *2 +2 *2 A28 A29 A30 +2 A31 x A32 x +2 A33 A34 A35 *2 A36 x +2 *2 *2 '
    postfix = 'A0 A1 x A2 A3 A4 A5 A6 x A7 x +2 A8 +2 *2 *2 A9 x *2 '
    # postfix = 'A B +'
    expr = postfix_to_tree(postfix)
    print(dimension(expr))

    printer = ExprPrint()
    printer.print_expr(expr)

    printer.drawio.write('test')


if __name__ == '__main__':
    main()
