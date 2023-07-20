Every element of a finite field Fp can be used to make a subgroup H under repeated action of multiplication. In other words, for an element g: H = {g, g^2, g^3, ...}

A primitive element of Fp is an element whose subgroup H = Fp, i.e., every element of Fp, can be written as g^n mod p for some integer n. Because of this, primitive elements are sometimes called generators of the finite field.

For the finite field with p = 28151 find the smallest element g which is a primitive element of Fp.

This problem can be solved by brute-force, but there's also clever ways to speed up the calculation.

we can use :
>>> from sympy import *

>>> 
>>> # Set the value of p
>>> p = 28151
>>> 
>>> # Find a primitive element of Fp
>>> g = primitive_root(p)
>>> 
>>> # Print the value of g
>>> print("A primitive element of Fp is:", g)
A primitive element of Fp is: 7


letus understand what happend and what is mean of primitive element
primitive element(root) or ganrator is the number or set of numbers that can used to generator the entire
Fp such that g^n mod p -> {1....p} so letus conseder that g=5 , p=17 so what i mean is :
Fp :
	1 = 5^1 mod 17
	2 = 5^6 mod 17
	3 = 5^13 mod 17
	4 = 5^12 mod 17
	5 = 5^1 mod 17
	6 = 5^3 mod 17 
	7 = 5^15 mod 17
	8 = 5^2 mod 17
	9 = 5^10 mod 17
	10 = 5^7 mod 17
	11 = 5^11 mod 17
	12 = 5^9 mod 17
	13 = 5^4 mod 17
	14 = 5^5 mod 17
	15 = 5^14 mod 17
	16 = 5^8 mod 17

	the resulte is unfirmally distrubute form 5^1mod17 -> 5^16 mod17 we got uniq resulte 
	and thit's why we say the 5 is primitive_root of 17  

	so we can brute force it:
def is_primitive(k, p):
	for i in range(2, p):
	    if pow(k, i, p) == k:
	        return False
	return True

for k in range(2, p):
    if is_primitive(k, p):
        print(k)
        break
>>>7


a more effiecient if we use a bool list 
def is_primitive(k, p):
	dublicate = [False] * p 
	for i in range(2, p):
		if dublicate[pow(k, i, p)]:
			return False
		dublicate[pow(k, i, p)] = True
	return True