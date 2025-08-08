from .misc import base_62
from .misc import roundings

radix = 10
width = 8
char_set = base_62

char_point = '.'
char_pos = '+'
char_neg = '-'
char_exp = 'e'
char_inf = '∞'
char_nan = '?'
pad_num = '0'
pad_inf = '_'
pad_nan = '_'
str_inf = 'inf'
str_nan = 'nan'

matrix_border_E  = '|'
matrix_border_N  = ''
matrix_border_W  = '|'
matrix_border_S  = ''
matrix_corner_NE = '┓'
matrix_corner_NW = '┏'
matrix_corner_SW = '┗'
matrix_corner_SE = '┛'
matrix_void_fill = ' '
matrix_div_row   = ' '
matrix_div_col   = ''
matrix_div_cross = '+'

rounding = roundings['half_to_even']
