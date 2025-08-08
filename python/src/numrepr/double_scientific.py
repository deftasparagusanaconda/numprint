from . import defaults 

def double_scientific(number, width=defaults.width):
	'print a float in scientific notation'
	if isinstance(number, float):
		output = '-' if number < 0 else '+'
		output += number.hex()
"""
print(0.5, double_scientific(0.5))
print(1.0, double_scientific(1.0))
print('pi ', double_scientific(3.14159265358979323846264338327950288419))
print(2.0, double_scientific(2.0))
print(double_scientific(2**-1030))
print(double_scientific(float('inf')))
"""
