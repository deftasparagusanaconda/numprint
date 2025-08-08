def digits_ratio(digits):
	'return ratio of mantissa digits to exponent digits. this formula is approximated from a pattern in the IEEE floats from 4-bit to 256-bit'
	return 0.58630968788*digits**0.71

def digits(digits):
	'return digits of mantissa and digits of exponent given a total number of digits'
	exp = round(digits/(1+digits_ratio(digits)))
	return digits-exp, exp

def round_random(x, digits=0):
	from random import randint
	from math import floor, ceil

	raise NotImplementedError
#	if 
#		return floor(x) if random.randint(0, 1) else ceil(x)

def round_stochastic(x, digits=0):
	raise NotImplementedError

roundings = {'half_to_even': round, 'random': round_random , 'stochastic': round_stochastic}

base_62 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
base_64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
base_64_url = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
dozenal = '0123456789↊↋'
ascii_all_printable = '␀␁␂␃␄␅␆␇␈␉␊␋␌␍␎␏␐␑␒␓␔␕␖␗␘␙␚␛␜␝␞␟␠!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~␡'
metric_prefixes = '.kMGTPEZYRQqryzafpnµm'
morse = '._'

test_cases = list()
for i in range(9, -1, -1):
	test_cases.append(-float(i))
for i in range(10):
	test_cases.append(i)
for i in range(9, 0, -1):
	test_cases.append(10**-i)
for i in range(10):
	test_cases.append(10**i)
for i in range(9, 0, -1):
	test_cases.append(10**-i)
for i in range(10):
	test_cases.append(10**i)
test_cases.append(2.0**-1074)
test_cases.append(1.0e-100)
test_cases.append(1.0e+100)
test_cases.append(2.0**1023)
test_cases.append(6.62607015e-34)
test_cases.append(9.1093837139e-31)
test_cases.append(0.5772156649015328606065)
test_cases.append(1.41421356237309504)
test_cases.append(1.7182818284590452353)
test_cases.append(3.14159265358979323846264338327950288419)
test_cases.append(299792458.0)
test_cases.append(6.02214076e+23)
test_cases.append(float('nan'))
test_cases.append(float('inf'))
test_cases.append(float('-inf'))
