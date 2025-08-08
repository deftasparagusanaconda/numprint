#from .fixed_width import fixed_width
from . import defaults
from .fixed_width import fixed_width

"""
defaults.matrix_div_row   = '|'
defaults.matrix_div_col   = '-'
defaults.matrix_div_cross = '+'
defaults.matrix_null_fill = ' '
defaults.matrix_border_E  = ' |'
defaults.matrix_border_N  = '-'
defaults.matrix_border_W  = '| '
defaults.matrix_border_S  = '-'
defaults.matrix_corner_NE = '┓'
defaults.matrix_corner_NW = '┏'
defaults.matrix_corner_SW = '┗'
defaults.matrix_corner_SE = '┛'
"""
#fixed_width = lambda a,b: str(a)[:defaults.width].zfill(defaults.width)

def matrix(mat:list[list[any]],
	width     :int = defaults.width,
	div_row   :str = defaults.matrix_div_row,
	div_col   :str = defaults.matrix_div_col,
	div_cross :str = defaults.matrix_div_cross,
	void_fill :str = defaults.matrix_void_fill,
	border_E  :str = defaults.matrix_border_E,
	border_N  :str = defaults.matrix_border_N,
	border_W  :str = defaults.matrix_border_W,
	border_S  :str = defaults.matrix_border_S,
	corner_NE :str = defaults.matrix_corner_NE,
	corner_NW :str = defaults.matrix_corner_NW,
	corner_SW :str = defaults.matrix_corner_SW,
	corner_SE :str = defaults.matrix_corner_SE,
	) -> str:
	'represent any matrix stored as [ [...], [...], [...], ... ]'

	if len(mat) == 0:
		return ''

	output = str()

	# in case of ragged matrix
	lengths = tuple(len(row) if hasattr(row,'__len__') else 0 for row in mat)
	max_length = max(lengths)	# is always >= 1

	# for top & bottom border widths
	total_width = max_length*width + (max_length-1)*len(div_row) + len(border_W) + len(border_E)

	# top border
	if border_N != '':
		output += corner_NW
		output += border_N[0]*(total_width-len(corner_NW)-len(corner_NE))
		output += corner_NE
		output += '\n'
		for c in border_N[1:]:
			output += border_W
			output += c*(total_width-len(border_W)-len(border_E))
			output += border_E
			output += '\n'

	# the main part!!
	for i in range(len(mat)-1):
		output += border_W
		output += fixed_width(mat[i][0], width) if hasattr(mat[i], '__iter__') else void_fill*width
		for j in range(1, lengths[i]):
			output += div_row
			output += fixed_width(mat[i][j], width)
		for j in range(max_length-lengths[i]):
			output += div_row
			output += void_fill*width
		output += border_E
		output += '\n'

		for c in div_col:
			output += border_W
			output += c*width
			for idfk in range(1, max_length):
				output += div_cross*len(div_row) + c*width
			output += border_E
			output += '\n'

	# print last row separately
	output += border_W
	output += fixed_width(mat[-1][0], width)
	for j in range(1, lengths[-1]):
		output += div_row
		output += fixed_width(mat[-1][j], width)
	for j in range(max_length-lengths[-1]):
		output += div_row
		output += null_fill*width
	output += border_E

	# bottom border
	if border_S != '':
		output += '\n'
		for c in border_S[:-1]:
			output += border_W
			output += c*(total_width-len(border_W)-len(border_E))
			output += border_E
			output += '\n'
		output += corner_SW
		output += border_S[-1]*(total_width-len(corner_SW)-len(corner_SE))
		output += corner_SE
	
	return output
"""
import random
thing = [None]*3
for i in range(3):
	thing[i] = [None]*3
	for j in range(3):
		num = 2**(random.random()*10)*(-1)**random.randint(0,1)
		thing[i][j] = num
print(matrix(thing))
"""
