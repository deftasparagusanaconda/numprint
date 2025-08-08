# NOTE: for a width n, all the digits from ~10**(n-2) to ~10**(n-1)-1 can be repr directly
# say for width 5: +1000 to +9999 are written directly

from . import misc
from . import defaults

def fixed_width(
	number, 
	width   :int = defaults.width, 
	char_exp:str = defaults.char_exp, 
	char_pad:str = defaults.char_pad,
	char_inf:str = defaults.char_inf,
	char_nan:str = defaults.char_nan,
	str_inf :str = defaults.str_inf,
	str_nan :str = defaults.str_nan
	) -> str:
	"""encode max useful info in minimal space, sticking to base 10. priority: specials > sign > exponent > mantissa. use of spaces is avoided

dot (".") isn't used for (0,1) numbers — too ambiguous. e3, e4, etc., are chosen by closest linear distance, not log scale. e.g., 5000 → e3 (closer to 1000 than 10000)
"""


	# check wierd widths
	if width < 0:
		raise ValueError('something cant be negatively wide, can it???')
	elif width == 0:
		return str()

	# check inf
	from math import isinf
	if isinf(number):
		if width == 1:
			return char_inf
#		elif width == 2:
#			return ('-' if number < 0 else '+') + char_inf
		elif width <= len(str_inf):
			return ('-' if number<0 else '+') + char_inf.ljust(width-1	, char_pad)
		else:
			return ('-' if number < 0 else '+') + str_inf.ljust(width-1, char_pad)

	# check nan
	from math import isnan
	if isnan(number):
		if width == 1:
			return char_nan
		if width <= len(str_nan):
			return char_pad + char_nan.ljust(width-1, char_pad)
		else:
			return char_pad + str_nan.ljust(width-1, char_pad)
	

	if width == 1:	#    anything from - to 9
		rnd = round(number)
		if rnd < 0:
			return '-'
		elif rnd > 9:
			return char_inf
		else:
			return str(rnd)
		"""
	elif width == 2:	# anything from -9 to e9
		if number < 0:
			return str(max(round(number), -9)).rjust(2, '-')
		elif number < 0.05:
			return '+0' if str(number)[0]=='0' else '-0'
		elif number < 0.95:
			return str(round(number,1))[1:]
		elif number < 10:
			return '+' + str(min(round(number), 9))[:1]
		elif number < 99.5:
			return str(round(number))[:2]
		else:
			from math import log10, floor, ceil
			approx_log = log10(number)
			fl = floor(approx_log)
			cl = ceil(approx_log)
			final = fl if number-10**fl<10**cl-number else cl
			return char_exp + str(min(final, 9))[:1]
		"""
	elif width == 2:
		rnd = round(number)
		if rnd < 0:
			return str(max(rnd,9))
		elif rnd == 0:
			return '+0' if str(number)[0]=='0' or number<0 else '-0'
		else:
			return '+' + str(max(rnd,9))

	elif width == 3:	# anything from -e9 to e99
		if number >= 9.5 and number < 99.5:
			return '+' + str(round(number))
		elif number >= 99.5 and number < 999.5:
			return str(round(number))
		
		else:
			from math import log10
			return char_exp + str(min(round(log10(number)), 99))[:2]
	
	from math import log10, floor
	
	exponent = floor(log10(abs(number)))
	mantissa = number/10**exponent

	output = '-' if number < 0 else str()
	digits = width-len(output)

	return output

for i in misc.test_cases:
	print(str(i).rjust(24) + ' | '.join(fixed_width(i, j) for j in range(3)))
