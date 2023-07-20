We've looked at multiplication and division in modular arithmetic, but what does it mean to take the square root modulo an integer?

For the following discussion, let's work modulo p = 29. We can take the integer a = 11 and calculate a2 = 5 mod 29.

As a = 11, a2 = 5, we say the square root of 5 is 11.
>>> for i in range(1,p):
...     if pow(i,2,29) == a2:
...             print(i)
... 
11
18


This feels good, but now let's think about the square root of 18. From the above, we know we need to find some integer a such that a2 = 18
>>> def find_squar_root(p,a2):
...     for i in range(1,p):
...             if pow(i,2,29) == a2:
...                     print(i)
>>> find_squar_root(p,18)
>>>
Your first idea might be to start with a = 1 and loop to a = p-1. In this discussion p isn't too large and we can quickly look.

Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all a ∈ Fp* you never find an a such that a2 = 18.

What we are seeing, is that for the elements of F*p, not every element has a square root. In fact, what we find is that for roughly one half of the elements of Fp*, there is no square root.

We say that an integer x is a Quadratic Residue if there exists an a such that a2 = x mod p. If there is no such solution, then the integer is a Quadratic Non-Residue.

In other words, x is a quadratic residue when it is possible to take the square root of x modulo an integer p.

In the below list there are two non-quadratic residues and one quadratic residue.

Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.

If a2 = x then (-a)2 = x. So if x is a quadratic residue in some finite field, then there are always two solutions for a.

p = 29
ints = [14, 6, 11] 
>>> find_squar_root(p,14)
>>> find_squar_root(p,6)
8
21
>>> find_squar_root(p,11)
>>> 
--------tonelli-shanks-------
what we use here is simple code, but tonelli-shanks more effiecient for find_squar_root
implementation:

import math
def tonelli_shanks(n, p):
    """
    Tonelli-Shanks algorithm
    Returns a modular square root of n modulo p.
    p must be an odd prime.
    """
    if pow(n, (p-1)//2, p) != 1:
        return None # n is not a square modulo p
    
    # Factor p-1 as Q * 2^S
    Q = p - 1
    S = 0
    while Q % 2 == 0:
        S += 1
        Q //= 2
    
    # Find a quadratic nonresidue mod p
    z = 2
    while pow(z, (p-1)//2, p) != p-1:
        z += 1
    
    # Initialize variables
    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q+1)//2, p)
    
    # Main loop
    while t != 1:
        i = 0
        temp = t
        while temp != 1 and i < M-1:
            temp = pow(temp, 2, p)
            i += 1
        
        b = pow(c, 2**(M-i-1), p)
        M = i
        c = pow(b, 2, p)
        t = (t * pow(b, 2, p)) % p
        R = (R * b) % p
    
    return R

a = 5
p = 29

if pow(a, (p-1)//2, p) == 1:
    root = tonelli_shanks(a, p)
    print("Square roots of", a, "mod", p, "are:", root, p-root)
else:
    print(a, "does not have a square root modulo", p)

output:Square roots of 5 mod 29 are: 18 11


resource:
https://www.youtube.com/watch?v=d7ZFCf95MAQ