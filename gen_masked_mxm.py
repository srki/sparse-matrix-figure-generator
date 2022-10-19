from util import *


def gen_masked_mxm():
    A = [[0, 0, 0, 0, 0, 0, 0, 6],
         [0, 0, 0, 0, 4, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 0, 3, 5, 0, 0, 2],
         [1, 9, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 7, 0, 0, 0, 0],
         [0, 5, 0, 0, 0, 0, 0, 1],
         [1, 0, 8, 0, 9, 0, 0, 0],
         ]

    B = [[1, 0, 0, 1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 1, 1, 0, 1, 1, 0],
         [1, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 1, 0],
         ]

    M = [[0, 1, 0, 0, 1, 0, 1, 1],
         [0, 0, 0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 1, 0, 1],
         [0, 0, 1, 0, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 1],
         ]

    A = random_matrices(8, 10, 15)
    B = random_matrices(10, 8, 15)
    M = random_matrices(8, 8, 15)

    C_tmp = []
    for i in range(0, len(A)):
        C_tmp.append([])
        for j in range(0, len(B[0])):
            v = 0
            for k in range(0, len(A[0])):
                v += A[i][k] * B[k][j]
            C_tmp[i].append(v)

    C = []
    for i in range(0, len(C_tmp)):
        C.append([])
        for j in range(0, len(C_tmp[0])):
            C[i].append(C_tmp[i][j] * M[i][j])

    write('show_zeros', create_document(add_matrix(0, 0, A, ORANGE_LIGHT, ORANGE_DARK, show_zeros=True, show_values=True)), )
    write('hide_zeros', create_document(add_matrix(0, 0, A, ORANGE_LIGHT, ORANGE_DARK, show_zeros=False, show_values=True)), )
    write('hide_values', create_document(add_matrix(0, 0, A, ORANGE_LIGHT, ORANGE_DARK, show_zeros=False, show_values=False)), )
    write('A', create_document(add_matrix(0, 0, A, ORANGE_LIGHT, ORANGE_DARK, show_zeros=False, show_values=False)))
    write('B', create_document(add_matrix(0, 0, B, BLUE_LIGHT, BLUE_DARK, show_zeros=False, show_values=False)))
    write('M', create_document(add_matrix(0, 0, M, RED_LIGHT, RED_DARK, show_zeros=False, show_values=False)))
    write('C_tmp', create_document(add_matrix(0, 0, C_tmp, PURPLE_LIGHT, PURPLE_DARK, show_zeros=False, show_values=False)))
    write('C', create_document(add_matrix(0, 0, C, GREEN_LIGHT, GREEN_DARK, show_zeros=False, show_values=False)))
    write('M_circle', create_document(add_matrix(0, 0, M, RED_LIGHT, RED_DARK, show_zeros=False, show_values=False)))


if __name__ == '__main__':
    gen_masked_mxm()
