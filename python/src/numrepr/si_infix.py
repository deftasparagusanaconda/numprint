from misc import metric_prefixes, dozenal

def si_infix(number,
	chars:int  = 4    , # number of characters to print
	base :int  = 10   , # which radix to use
	sign :bool = True , # print sign
	use_u:bool = False, # use u instead of µ
	use_K:bool = False, # use K instead of k
	num_char_set:list[str] = dozenal, # which set of numbers to use
	infix:list[str]  = metric_prefixes, # which set of infixes to use
	) -> str:
	"print a number as a fixed number of characters"

	if number == float('inf'):
		return 
	
	if not sign and number < 0:
		raise ValueError("cannot represent -ve number without signage)")
	
	digits = chars - 1 - sign # since a bool is just an int
	
	raise NotImplementedError


