# numprint

a cross-language library to display numbers in different representations

<details><summary>radix</summary>

convert to base 10 (decimal), base 2 (binary), base 12 (dozenal), base 36 (alphanumeric), base 62, base 127, etc etc.

</details><details><summary>prime factors</summary>

convert to prime factors

also supports array output
  
</details><details><summary>si infix</summary>
```
|         original          | 3ch | 4chr | 5char | 4alt | 5altr |
| 12,345,000                | 12M | 12M3 | 12M34 | 12M3 | 12M34 |
|  1,234,500                | 1M2 | 1M23 | 1M234 | 1M23 | 1M234 |
|    123,450                | M12 | M123 | M1234 | 123K | 123K4 |
|     12,345                | 12K | 12K3 | 12K34 | 12K3 | 12K34 |
|      1,234.5              | 1K2 | 1K23 | 1K234 | 1K23 | 1K234 |
|        123.45             | K12 | K123 | K1234 | 123. | 123.4 |
|         12.345            | 12. | 12.3 | 12.34 | 12.3 | 12.34 |
|          1.234,5          | 1.2 | 1.23 | 1.234 | 1.23 | 1.234 |
|          0.123,45         | .12 | .123 | .1234 | 123m | 123m4 |
|          0.012,345        | 12m | 12m3 | 12m34 | 12m3 | 12m34 |
|          0.001,234,5      | 1m2 | 1m23 | 1m234 | 1m23 | 1m234 |
|          0.000,123,45     | m12 | m123 | m1234 | 123n | 123n4 |
|          0.000,012,345    | 12n | 12n3 | 12n34 | 12n3 | 12n34 |
|          0.000,001,234,5  | 1n2 | 1n23 | 1n234 | 1n23 | 123n4 |
|          0.000,000,123,45 | n12 | n123 | n1234 | 123u | 123u4 |
```
Q quetta 	10^30
R ronna 	10^27
Y yotta 	10^24
Z zetta  	10^21
E exa 	 	10^18
P peta 	 	10^15
T tera 	 	10^12
G giga 	 	10^9
M mega 	 	10^6
k kilo 		10^3   K is used instead of k
H hecto  	10^2   not used
D deca 	 	10^1   not used
. point   10^0
d deci 	 	10^-1  not used
c centi  	10^-2  not used
m milli  	10^-3
μ micro  	10^-6  u is used instead of μ
n nano 	 	10^-9
p pico 		10^-12
f femto  	10^-15
a atto 	 	10^-18
z zepto 	10^-21
y yocto 	10^-24
r ronto 	10^-27
q quecto  10^-30

SI prefix colours are calculated according to hpluv(x,100,76)

links:
https://en.wikipedia.org/wiki/Metric_prefix
https://www.hsluv.org/

i hope that was explanatory... i hope..

in general, a number like `123,450` can be written as `000M123K450.000m000n000` and we simply take n characters from the first significant number (or the SI prefix next to it)
</details>

mathy nerd~  
\- [daa][https://github.com/deftasparagusanaconda]
