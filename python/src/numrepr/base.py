from . import defaults
from .misc import *

def base(
	number,
	base:int=defaults.radix,         # desired radix
	char_set:str=defaults.char_set, # desired characters
	) -> str:

	while number >= 1:   # integer part
		output = char_set[number % base] + output
		number //= base
	
	if number < 0:
		return '-' + output
	return output
