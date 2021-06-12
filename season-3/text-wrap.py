""" Se le da una cadena S y un ancho w.
Su tarea es formatear la cadena en un párrafo de ancho w. """
import textwrap
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width = max_width)
    word_list = wrapper.wrap(text = string)
    return "\n".join(word_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Test input:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Output:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ