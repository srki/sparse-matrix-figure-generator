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


class DrawIo:

    def __init__(self):
        self.content = ''
        self.id = 0
        pass

    @staticmethod
    def subscript(text):
        return f'&lt;sub&gt;{text}&lt;/sub&gt;'

    def add_text_box(self, x, y, value, font_color='#0000000'):
        elem_id = self.get_next_id()
        self.content += f'<mxCell id="{elem_id}" value="{value}" ' \
                        f'style="text;html=1;strokeColor=none;fillColor=none;align=center;' \
                        f'verticalAlign=middle;whiteSpace=wrap;rounded=0;' \
                        f'fontSize=32;fontStyle=1;fontColor={font_color};" ' \
                        f'vertex="1" parent="1">\n' \
                        f'<mxGeometry x="{x}" y="{y}" width="40" height="40" as="geometry" />\n' \
                        '</mxCell>\n'

    def add_rectangle_text(self, x, y, w, h, value, fill_color, stroke_color, stroke_width, font_size=16,
                           font_color='#0000000'):
        elem_id = self.get_next_id()
        self.content += f'<mxCell id="{elem_id}" value="{value}" style="text;html=1;' \
                        f'strokeColor={stroke_color};strokeWidth={stroke_width};fillColor={fill_color};' \
                        f'align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;' \
                        f'fontSize={font_size};fontStyle=1;fontColor={font_color};" ' \
                        f'vertex="1" parent="1">\n' \
                        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" />\n' \
                        '</mxCell>\n'

    def add_dot(self, x, y):
        elem_id = self.get_next_id()
        self.content += f'<mxCell id="{elem_id}" value="" ' \
                        f'style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;' \
                        f'fontColor=#333333;fillColor=#000000;" ' \
                        f'parent="1" vertex="1">\n' \
                        f'<mxGeometry x="{x}" y="{y}" width="20" height="20" as="geometry" />\n' \
                        '</mxCell>\n'

    def add_circle(self, x, y, value=''):
        elem_id = self.get_next_id()
        self.content += f'<mxCell id="{elem_id}" value="{value}" style="ellipse;whiteSpace=wrap;html=1;fontSize=18;' \
                        'strokeColor=#b85450;fillColor=none;strokeWidth=5;" vertex="1" parent="1">\n' \
                        f'<mxGeometry x="{x}" y="{y}" width="34" height="34" as="geometry" />\n' \
                        '</mxCell>'
        return elem_id

    def add_rectangle(self, x, y, w, h, fill_color, stroke_color):
        elem_id = self.get_next_id()
        self.content += f'<mxCell id="{elem_id}" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor={fill_color}' \
                        f';strokeWidth=3;strokeColor={stroke_color};" parent="1" vertex="1">\n' \
                        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" />\n' \
                        '</mxCell>\n'

    def add_label(self, x, y, w, text):
        elem_id = self.get_next_id()
        self.content += f'<mxCell  id="{elem_id}" value="&lt;font style=&quot;font-size: 50px&quot;&gt;{text}&lt;/font&gt;" ' \
                        f'style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;' \
                        f'whiteSpace=wrap;rounded=0;fontSize=30;fontStyle=1" parent="1" vertex="1">\n' \
                        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="60" as="geometry" />\n' \
                        '</mxCell>\n'

    def add_link(self, src_id, dst_id, exit_x, exit_y):
        elem_id = self.get_next_id()
        self.content = f'<mxCell id="{elem_id}" ' \
                        f'style="rounded=0;orthogonalLoop=1;jettySize=auto;' \
                        f'html=1;exitX={exit_x};exitY={exit_y};exitDx=0;exitDy=0;" ' \
                        f'edge="1" parent="1" ' \
                        f'source="{src_id}" target="{dst_id}">' \
                        f'<mxGeometry relative="1" as="geometry" />' \
                        f'</mxCell>' + self.content
        return elem_id

    def create_document(self):
        return '<mxGraphModel dx="1106" dy="738" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" ' \
               'arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">\n' \
               '<root>\n' \
               '<mxCell id="0" />\n' \
               '<mxCell id="1" parent="0" />\n' \
               f'{self.content}\n' \
               '</root>\n' \
               '</mxGraphModel>\n'

    def write(self, name):
        if not os.path.exists('xml'):
            os.mkdir('xml')

        if not os.path.exists('img'):
            os.mkdir('img')

        a = open(f'xml/{name}.drawio', 'w')
        a.write(self.create_document())
        a.close()
        # os.system(f'/Applications/draw.io.app/Contents/MacOS/draw.io xml/{name}.drawio -t -x -o img/{name}.png')
        os.system(f'/snap/bin/drawio xml/{name}.drawio -t -x -o img/{name}.pdf')

    def get_next_id(self):
        next_id = "4a69013be9f08507faccbecfd71a06e9" + str(self.id)
        self.id += 1
        return next_id
