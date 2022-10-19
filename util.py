import os
import random

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


def write(name, content):
    if not os.path.exists('xml'):
        os.mkdir('xml')

    if not os.path.exists('img'):
        os.mkdir('img')

    a = open(f'xml/{name}.drawio', 'w')
    a.write(content)
    a.close()
    # os.system(f'/Applications/draw.io.app/Contents/MacOS/draw.io xml/{name}.drawio -t -x -o img/{name}.png')
    # os.system(f'/snap/bin/drawio xml/{name}.drawio -t -x -o img/{name}.png')


def random_matrices(n, m, nnz, low_value=1, hi_value=1, seed=0):
    if seed:
        random.seed(seed)

    matrix = []
    for i in range(0, n):
        matrix.append([0 for j in range(0, m)])

    for i in range(0, nnz):
        matrix[random.randrange(0, n)][random.randrange(0, m)] = random.randint(low_value, hi_value)

    return matrix
