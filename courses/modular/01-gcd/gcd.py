# **native algo =>O(min(a,b)) **
def gcd(a,b):
	gcd_num=1
	a_divation=get_divisors(a)
	b_divation=get_divisors(b)
	#no need for sort , it sorted by defulat
	# sorted(a_divation)
	# sorted(b_divation)
	print(a_divation)
	print(b_divation)
	bigger=get_bigger(a_divation,b_divation)
	if bigger == 'a':
		for i in a_divation:
			if i in b_divation:
				gcd_num=i
	else:
		for i in b_divation:
			if i in a_divation:
				gcd_num=i
	return gcd_num

"""
12
1,2,3,4,8,12
"""
def get_divisors(n):
	div=[]
	for i in range(1,int(n/2)+1):
		if n%i==0:
			div.append(i) 
	div.append(n)
	return div

def get_bigger(a,b):
	if len(a) >= len(b):
		return 'a'
	else:
		return 'b'

print(gcd(26513,32321))

#---------------------------------------------------------------------------------------------------------------------------------------------

#**Euclid's Algorithm. => O(log min(a,b))**

def euclid_gcd(a, b):
    """
    Compute the GCD of two positive integers using Euclid's Algorithm.

    Args:
    a (int): The first positive integer.
    b (int): The second positive integer.

    Returns:
    int: The GCD of a and b.
    """
    # Ensure a is greater than b
    if b > a:
        a, b = b, a
    
    # Find the GCD using Euclid's Algorithm
    while b != 0:
        r = a % b
        a = b
        b = r
    
    return a
"""
Here's how the function works:

The function takes two positive integers a and b as input.
If b is greater than a, the values of a and b are swapped to ensure that a is greater than b.
The function then uses Euclid's Algorithm to find the GCD of a and b. The algorithm works as follows:
If b is zero, then a is the GCD of a and b.
Otherwise, compute the remainder r when a is divided by b.
Set a to b, and set b to r.
Repeat until b is zero.
The function returns the value of a, which is the GCD of a and b.
"""
print(euclid_gcd(26513,32321))

"""
explain why it faster:
To see why Euclid's Algorithm is faster than the naive algorithm, consider the example of finding the GCD of 300 and 75. With the naive algorithm, we would need to check every integer between 1 and 75 to see if it divides both 300 and 75 evenly. This would require 75 iterations, which is quite slow.

With Euclid's Algorithm, we can find the GCD much faster. The algorithm works by repeatedly taking the remainder of the larger number divided by the smaller number, until the remainder is 0. In this case, we would perform the following steps:

Divide 300 by 75, yielding a quotient of 4 and a remainder of 0. Therefore, the GCD is 75.
As you can see, Euclid's Algorithm requires only one iteration to find the GCD of 300 and 75, whereas the naive algorithm would require 75 iterations. This demonstrates why Euclid's Algorithm is much faster than the naive algorithm for finding the GCD of two positive integers.
"""

#:)
def one_line_gcd(a,b):return one_line_gcd(b%a,a) if a else b
# print(one_line_gcd(66528,52920))