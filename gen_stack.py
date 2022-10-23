from util import *

width = 320
height = 80


def gen_elem(x, y, text, color, font_size=32):
    colors = {
        'blank': {'none', 'none'},
        'orange': (ORANGE_LIGHT, ORANGE_DARK),
        'blue': (BLUE_LIGHT, BLUE_DARK),
        'red': (RED_LIGHT, RED_DARK),
        'purple': (PURPLE_LIGHT, PURPLE_DARK),
        'green': (GRAY_LIGHT, GRAY_DARK),
        'gray': (GRAY_LIGHT, GRAY_DARK),
    }

    fill_color, stroke_color = colors[color]
    return add_rectangle_text(x, y, width, height-4, text, fill_color=fill_color,
                              stroke_color=stroke_color, stroke_width=5, font_size=font_size)


def main():
    stack_empty_1 = gen_elem(0, 0, '', 'gray')
    stack_empty_0 = gen_elem(0, height, '', 'gray')
    stack_empty_vec_0 = gen_elem(0, height, 'reserved', 'purple')
    stack_a_1 = gen_elem(0, 0, f'A{subscript("i,*")}', 'orange')
    stack_axb_0 = gen_elem(0, height, f'A{subscript("i,*")}B', 'blue')
    stack_sel_axb_0 = gen_elem(0, height, f'select(f{subscript(1)}, A{subscript("i,*")}B)', 'blue')
    stack_c_1 = gen_elem(0, 0, f'C{subscript("i,*")}', 'orange')
    stack_apply_c_1 = gen_elem(0, 0, f'apply(f{subscript(2)}, C{subscript("i,*")})', 'blue')
    stack_sel_axb_apply_c_0 = gen_elem(0, height, f'select(f{subscript(1)}, A{subscript("i,*")}B) '
                                                  f'⊕ apply(f{subscript(2)}, C{subscript("i,*")})', 'blue', 20)

    write('stack-0', create_document(stack_empty_0 + stack_empty_1))
    write('stack-1', create_document(stack_empty_vec_0 + stack_empty_1))
    write('stack-2', create_document(stack_empty_vec_0 + stack_a_1))
    write('stack-3', create_document(stack_axb_0 + stack_empty_1))
    write('stack-4', create_document(stack_sel_axb_0 + stack_empty_1))
    write('stack-5', create_document(stack_sel_axb_0 + stack_c_1))
    write('stack-6', create_document(stack_sel_axb_0 + stack_apply_c_1))
    write('stack-7', create_document(stack_sel_axb_apply_c_0 + stack_empty_1))


if __name__ == '__main__':
    main()
