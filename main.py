import os

ORANGE_LIGHT = '#FFE6CC'
ORANGE_DARK = '#D79B00'
BLUE_LIGHT = '#DAE8FC'
BLUE_DARK = '#6C8EBF'
RED_LIGHT = '#F8CECC'
RED_DARK = '#B85450'
PURPLE_LIGHT = '#E1D5E7'
PURPLE_DARK = '#9673A6'
GREEN_LIGHT = '#D5E8D4'
GREEN_DARK = '#82B366'
GRAY_LIGHT = '#F5F5F5'
GRAY_DARK = '#666666'


def add_text_box(x, y, value, font_color='#0000000'):
    return f'<mxCell value="{value}" style="text;html=1;strokeColor=none;fillColor=none;align=center;' \
           f'verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=32;fontStyle=1;fontColor={font_color};" ' \
           f'vertex="1" parent="1">\n' \
           f'<mxGeometry x="{x}" y="{y}" width="40" height="40" as="geometry" />\n' \
           '</mxCell>\n'


def add_dot(x, y):
    return '<mxCell value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fontColor=#333333;fillColor=#000000;"' \
           ' parent="1" vertex="1">\n' \
           f'<mxGeometry x="{x}" y="{y}" width="20" height="20" as="geometry" />\n' \
           '</mxCell>\n'


def add_circle(x, y):
    return '<mxCell value="" style="ellipse;whiteSpace=wrap;html=1;fontSize=32;' \
           'strokeColor=#b85450;fillColor=none;strokeWidth=5;" vertex="1" parent="1">\n' \
           f'<mxGeometry x="{x}" y="{y}" width="34" height="34" as="geometry" />\n' \
           '</mxCell>'


def add_rectangle(x, y, w, h, fill_color, stroke_color):
    return f'<mxCell value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor={fill_color}' \
           f';strokeWidth=3;strokeColor={stroke_color};" parent="1" vertex="1">\n' \
           f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" />\n' \
           '</mxCell>\n'


def add_label(x, y, w, text):
    return f'<mxCell value="&lt;font style=&quot;font-size: 50px&quot;&gt;{text}&lt;/font&gt;" ' \
           f'style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;' \
           f'whiteSpace=wrap;rounded=0;fontSize=30;fontStyle=1" parent="1" vertex="1">\n' \
           f'<mxGeometry x="{x}" y="{y}" width="{w}" height="60" as="geometry" />\n' \
           '</mxCell>\n'


def add_matrix(x_off, y_off, matrix, fill_color, stroke_color, show_zeros=False, show_values=False, show_rc=False):
    m = ''

    nrows = len(matrix)
    ncols = len(matrix[0])

    if show_rc:
        for i in range(0, nrows):
            m += add_text_box(x_off + i * 40 + 40, y_off, str(i + 1))

        for j in range(0, ncols):
            m += add_text_box(x_off, y_off + j * 40 + 40, str(j + 1))

        # m += add_label(x_off, y_off + (nrows + 1) * 40, (ncols + 1) * 40, 'matrix')

        x_off += 40
        y_off += 40

    m += add_rectangle(x_off, y_off, ncols * 40, nrows * 40, fill_color, stroke_color)
    for i in range(0, nrows):
        for j in range(0, ncols):
            val = matrix[i][j]
            if val == 0:
                if show_zeros and show_values:
                    m += add_text_box(x_off + j * 40, y_off + i * 40, str(matrix[i][j]), '#888888')
            else:
                if show_values:
                    m += add_text_box(x_off + j * 40, y_off + i * 40, str(matrix[i][j]))
                else:
                    m += add_dot(x_off + 10 + j * 40, y_off + 10 + i * 40)
                    # m += add_circle(x_off + 3 + j * 40, y_off + 3 + i * 40)

    return m


def create_document(content):
    return '<mxGraphModel dx="1106" dy="738" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">\n' \
           '<root>\n' \
           '<mxCell id="0" />\n' \
           '<mxCell id="1" parent="0" />\n' \
           f'{content}\n' \
           '</root>\n' \
           '</mxGraphModel>\n'


def create(content, name):
    if not os.path.exists('xml'):
        os.mkdir('xml')

    if not os.path.exists('img'):
        os.mkdir('img')

    a = open(f'xml/{name}.drawio', 'w')
    a.write(content)
    a.close()
    os.system(f'/Applications/draw.io.app/Contents/MacOS/draw.io xml/{name}.drawio -t -x -o img/{name}.png')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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

    create(create_document(add_matrix(0, 0, A, ORANGE_LIGHT, ORANGE_DARK, show_zeros=True, show_values=True)), 'show_zeros')
    create(create_document(add_matrix(0, 0, A, ORANGE_LIGHT, ORANGE_DARK,  show_zeros=False, show_values=True)), 'hide_zeros')
    create(create_document(add_matrix(0, 0, A, ORANGE_LIGHT, ORANGE_DARK,  show_zeros=False, show_values=False)), 'hide_values')
    create(create_document(add_matrix(0, 0, A, ORANGE_LIGHT, ORANGE_DARK,  show_zeros=False, show_values=False)), 'A')
    create(create_document(add_matrix(0, 0, B, BLUE_LIGHT, BLUE_DARK,  show_zeros=False, show_values=False)), 'B')
    create(create_document(add_matrix(0, 0, M, RED_LIGHT, RED_DARK, show_zeros=False, show_values=False)), 'M')
    create(create_document(add_matrix(0, 0, C_tmp, PURPLE_LIGHT, PURPLE_DARK, show_zeros=False, show_values=False)),'C_tmp')
    create(create_document(add_matrix(0, 0, C, GREEN_LIGHT, GREEN_DARK, show_zeros=False, show_values=False)), 'C')
    create(create_document(add_matrix(0, 0, M, RED_LIGHT, RED_DARK, show_zeros=False, show_values=False)), 'M_circle')

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

    create(create_document(add_matrix(0, 0, graph, RED_LIGHT, RED_DARK, show_zeros=False, show_values=False, show_rc=True)), 'graph')
    create(create_document(add_matrix(0, 0, graphT, RED_LIGHT, RED_DARK, show_zeros=False, show_values=False, show_rc=True)), 'graphT')

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

    create(create_document(add_matrix(0, 0, unvisited1, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=False, show_rc=False)), 'unvisited1')
    create(create_document(add_matrix(0, 0, unvisited2, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=False, show_rc=False)), 'unvisited2')
    create(create_document(add_matrix(0, 0, unvisited3, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=False, show_rc=False)), 'unvisited3')

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

    create(create_document(add_matrix(0, 0, wavefront1, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=False, show_rc=False)), 'wavefront1')
    create(create_document(add_matrix(0, 0, wavefront2, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=False, show_rc=False)), 'wavefront2')
    create(create_document(add_matrix(0, 0, wavefront3, GRAY_LIGHT, GRAY_DARK, show_zeros=False, show_values=False, show_rc=False)), 'wavefront3')

