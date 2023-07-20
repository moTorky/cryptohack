'''
all we need is to find 101^17 mod 22663
'''
import math
print(pow(101,17,22663))

#or
num=101
po=17
md=22663
out=1
for i in range(po):
	out*=(num%md)
	out%=md
print(out)

'''
Modular exponentiation
given b = 4, e = 13, and m = 497:

    c ≡ 4^13 (mod 497)

One could use a calculator to compute 413; this comes out to 67,108,864. Taking this value modulo 497, the answer c is determined to be 445. 

In strong cryptography, b is often at least 1024 bits. Consider b = 5 × 10^76 and e = 17, both of which are perfectly reasonable values. 
In this example, b is 77 digits in length and e is 2 digits in length, but the value be is 1,304 decimal digits in length.
'''


'''
Trapdoor function
a trapdoor function is a function that is easy to compute in one direction, yet difficult to compute in the opposite direction, without special information,
An example of a simple mathematical trapdoor is "6895601 is the product of two prime numbers. 
What are those numbers?" A typical "brute-force" solution would be to try dividing 6895601 by several prime numbers until finding the answer.
'''