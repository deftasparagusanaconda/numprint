from miscellaneous import metric_prefixes, dozenal

def fixed_width(input,
	chars:int  = 4    , # number of characters to print
	ascii:bool = False, # if True, convert μ to u
	sign :bool = True , # print sign
	use_u:bool = False, # use u instead of µ
	use_K:bool = False, # use K instead of k
	base :int  = 10,              # which radix to use
	numch:str  = dozenal,         # which set of numbers to use
	infix:str  = metric_prefixes, # which set of infixes to use
	) -> str:
	"""print a number as a fixed number of characters"""
	
	if not sign and input < 0:
		raise ValueError("cannot represent -ve number without signage)")
	
    digits = chars - 1 - sign # since a bool is just an int
	

