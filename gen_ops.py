from util import *
import numpy as np


def ewise_add(a, b):
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[0])):
            c[i].append(a[i][j] + b[i][j])

    return c


def ewise_mult(a, b):
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[0])):
            c[i].append(a[i][j] * b[i][j])

    return c


def mxm(a, b):
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(b[0])):
            v = 0
            for k in range(len(a[0])):
                v += b[i][k] * b[k][j]
            c[i].append(v)

    return c


def apply(a, f):
    c = []
    for row in a:
        c.append([])
        for e in row:
            c[-1].append(f(e))
            e += 1
    return c


def gen_binary(seed=23536):
    while True:
        a = random_matrices(5, 5, 8, 1, 5, seed)
        a_xml = add_matrix(40, 40, a, ORANGE_LIGHT, ORANGE_DARK, show_zeros=False, show_values=True, show_rc=False)

        b = random_matrices(5, 5, 8, 1, 5, seed + 1)
        b_xml = add_matrix(320, 40, b, BLUE_LIGHT, BLUE_DARK, show_zeros=False, show_values=True, show_rc=False)

        if np.count_nonzero(ewise_mult(a, b)) >= 4 and np.max(ewise_mult(a, b)) < 10 \
                and np.max(mxm(a, b)) < 10 and 5 <= np.count_nonzero(mxm(a, b)) <= 8 \
                and 2 <= np.sum(a) / np.count_nonzero(a) <= 3 and 2 <= np.sum(b) / np.count_nonzero(b) <= 3:
            print(seed)
            break
        seed += 1

    c = ewise_add(a, b)
    c_xml = add_matrix(600, 40, c, GREEN_LIGHT, GREEN_DARK, show_zeros=False, show_values=True, show_rc=False)
    write('op-eWiseAdd', create_document(a_xml + b_xml + c_xml))

    c = ewise_mult(a, b)
    c_xml = add_matrix(600, 40, c, GREEN_LIGHT, GREEN_DARK, show_zeros=False, show_values=True, show_rc=False)
    write('op-eWiseMult', create_document(a_xml + b_xml + c_xml))

    c = mxm(a, b)
    c_xml = add_matrix(600, 40, c, GREEN_LIGHT, GREEN_DARK, show_zeros=False, show_values=True, show_rc=False)
    write('op-mxm', create_document(a_xml + b_xml + c_xml))
    return seed


def gen_unary(seed=23536):
    a = random_matrices(5, 5, 8, 1, 5, seed)
    a_xml = add_matrix(40, 40, a, ORANGE_LIGHT, ORANGE_DARK, show_zeros=False, show_values=True, show_rc=False)

    c = apply(a, lambda x: x + 2 if x != 0 else 0)
    c_xml = add_matrix(320, 40, c, GREEN_LIGHT, GREEN_DARK, show_zeros=False, show_values=True, show_rc=False)
    write('op-apply', create_document(a_xml + c_xml))

    c = apply(a, lambda x: x if x % 2 == 1 else 0)
    c_xml = add_matrix(320, 40, c, GREEN_LIGHT, GREEN_DARK, show_zeros=False, show_values=True, show_rc=False)
    write('op-select', create_document(a_xml + c_xml))


def reduction(seed=23536):
    a = random_matrices(5, 5, 8, 1, 5, seed)
    a_xml = add_matrix(40, 40, a, ORANGE_LIGHT, ORANGE_DARK, show_zeros=False, show_values=True, show_rc=False)

    c = np.sum(a)
    c_xml = add_text_box(320, 120, c)
    write('op-reduce', create_document(a_xml + c_xml))


def main():
    seed = 23536
    seed = gen_binary(seed)
    gen_unary(seed)
    reduction(seed)


if __name__ == '__main__':
    main()
