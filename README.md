# numprint

a cross-language library to display numbers in different representations

<details><summary>radix</summary>

convert to base 10 (decimal), base 2 (binary), base 12 (dozenal), base 36 (alphanumeric), base 62, base 127, etc etc.

</details><details><summary>prime_factors</summary>

convert to prime factors

also supports array output
  
</details><details><summary>fixed_width</summary>

its hard to explain what this thing does. just look at this:
```
         example          | 4chr | 5char | 6-char 
--------------------------+------+-------+--------
12,345,000                | +12M | +12M3 | +12M34  
-1,234,500                | -1M2 | -1M23 | -1M234  
   123,450                | +M12 | +M123 | +M1234  
   -12,345                | -12k | -12k3 | -12k34  
     1,234.5              | +1k2 | +1k23 | +1k234  
      -123.45             | -k12 | -k123 | -k1234  
        12.345            | +12. | +12.3 | +12.34  
        -1.234,5          | -1.2 | -1.23 | -1.234  
         0.123,45         | +.12 | +.123 | +.1234  
        -0.012,345        | -12m | -12m3 | -12m34  
         0.001,234,5      | +1m2 | +1m23 | +1m234  
        -0.000,123,45     | -m12 | -m123 | -m1234  
         0.000,012,345    | +12μ | +12μ3 | +12μ34  
        -0.000,001,234,5  | -1μ2 | -1μ23 | -1μ234  
         0.000,000,123,45 | +μ12 | +μ123 | +μ1234  
         0.0000000000...1 | +q00 | +q000 | +q0000 (very small but non-zero)
        -0.0000000000...1 | -q00 | -q000 | -q0000 (very small but non-zero)
+9...99999.99999999999999 | +99Q | +999Q | +9999Q (very big)
-9...99999.99999999999999 | -99Q | -999Q | -9999Q (very big)
        +0                | +000 | +0000 | +00000 (positive zero)
        -0                | -000 | -0000 | -00000 (negative zero)
      +inf                | +inf | +inf. | +inf.0 (positive infinity)
      -inf                | -inf | -inf. | -inf.0 (negative infinity)
      qnan                | qnan | qnan. | qnan.0 (quiet nan)
      snan                | snan | snan. | snan.0 (signalling nan)

where:
m = milli  (10^-3)  | k kilo   (10^3)
μ = micro  (10^-6)  | M mega   (10^6)
n = nano   (10^-9)  | G giga   (10^9)
p = pico   (10^-12) | T tera   (10^12)
f = femto  (10^-15) | P peta   (10^15)
a = atto   (10^-18) | E exa    (10^18)
z = zepto  (10^-21) | Z zetta  (10^21)
y = yocto  (10^-24) | Y yotta  (10^24)
r = ronto  (10^-27) | R ronna  (10^27)
q = quecto (10^-30) | Q quetta (10^30)
```

 fixed_width tries to show the most amount of information in a fixed amount of characters without resorting to alternate bases. it can also represent IEEE floating point numbers like `+inf` `-inf` `nan`, and signed zeroes `+0.0` `-0.0`
  
by default, it prints numbers using a metric prefix as an infix to encode both the decimal point and the exponent. if that is not enough, it can encode numerals to the mantissa and alphabets to the exponent, with the orders of magnitude between alphabets being the number of characters. 
```python
def fixed_width(
    ascii:bool = False, # if True, convert μ to u
    chars:int  = 4    , # number of characters to print
    sign :bool = True ) # print signage of number. setting False disallows negative input

    if sign is True:
        digits = chars - 2 # number of significant digits
    else:
        digits = chars - 1

    raise NotImplementedError
```
for predictability, representing numbers larger than `+99Q` as `+Qk1` or `+QQ1` or `+QQQ` will not be implemented.

SI prefix colours are calculated according to hpluv(x,100,76)

links:
https://en.wikipedia.org/wiki/Metric_prefix
https://www.hsluv.org/

i hope that was explanatory... i hope..

in general, a number like `123,450` can be written as `000M123K450.000m000n000` and we simply take n characters from the first significant number (or the SI prefix next to it)
</details>

mathy nerd~  
\- [daa][https://github.com/deftasparagusanaconda]
