from util import *


def gen_bfs():
    graph = [[0, 1, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 0, 0, 1, 0],
             [1, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0],
             [0, 0, 1, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0]]

    graphT = [[0, 0, 0, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 1, 1],
              [1, 0, 0, 0, 0, 0, 1],
              [0, 1, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 0, 0]]

    write('graph', create_document(
        add_matrix(0, 0, graph, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=True, show_rc=True)))
    write('graphT', create_document(
        add_matrix(0, 0, graphT, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=True, show_rc=True)))

    unvisited1 = [[1],
                  [1],
                  [1],
                  [1],
                  [1],
                  [1],
                  [1]]

    unvisited2 = [[0],
                  [1],
                  [1],
                  [1],
                  [1],
                  [1],
                  [1]]

    unvisited3 = [[0],
                  [0],
                  [1],
                  [0],
                  [1],
                  [1],
                  [1]]

    write('unvisited1', create_document(
        add_matrix(0, 0, unvisited1, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=True, show_rc=False)))
    write('unvisited2', create_document(
        add_matrix(0, 0, unvisited2, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=True, show_rc=False)))
    write('unvisited3', create_document(
        add_matrix(0, 0, unvisited3, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=True, show_rc=False)))

    wavefront1 = [[1],
                  [0],
                  [0],
                  [0],
                  [0],
                  [0],
                  [0]]

    wavefront2 = [[0],
                  [1],
                  [0],
                  [1],
                  [0],
                  [0],
                  [0]]

    wavefront3 = [[0],
                  [0],
                  [1],
                  [0],
                  [1],
                  [0],
                  [1]]

    write('wavefront1', create_document(
        add_matrix(0, 0, wavefront1, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=False, show_rc=False)))
    write('wavefront2', create_document(
        add_matrix(0, 0, wavefront2, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=False, show_rc=False)))
    write('wavefront3', create_document(
        add_matrix(0, 0, wavefront3, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=False, show_rc=False)))


if __name__ == '__main__':
    gen_bfs()
