for Diffie-Hellman we choose :
		g => small prime number
		n => very-big prime number like (2000-bit or now 4000-bits) 

		a => first-prive-key (for alice) random between 1->n 
		b => second-prive-key (for Bob) random between 1->n 

		in alice part(alice public-key)-> g^a mod n 
		in bob part(bob public-key)) -> g^b mod n

		then alice and bob share the puclic keys ,

		now alice have a and P-A -> g^(ab) mod n 
		bob have b, P-B ->> g^(ab) mod n 
		u can see wikibedia for small number and exambles 



The set of integers modulo n, together with the operations of both addition and multiplication is a ring. 
This means that adding or multiplying any two elements in the set returns another element in the set.

When the modulus is prime: n = p, we are guaranteed an inverse of every element in the set, 
and so the ring is promoted to a field. We refer to this field as a finite field Fp.

The Diffie-Hellman protocol works with elements of some finite field Fp, 
where the prime modulus is typically a large prime.
Given the prime p = 991, and the element g = 209, find the inverse element d such that g * d mod 991 = 1. 
>> while ((p*i)+1)%g:
...     i+=1
... 
>>> i
120
>>> ((p*i)+1)%g
0
>>> ((p*i)+1)/g
569.0
>>> 569*g
118921
>>> 118921%p
1
so d=569

if we complite looping we find other posiable values of d
>>> i+=1
>>> while ((p*i)+1)%g:
...     i+=1
... 
>>> i
329
>>> (329*p)+1
326040
>>> 326040/g
1560.0   ====>d
>>> i+=1
>>> while ((p*i)+1)%g:
...     i+=1
... 
>>> (p*i)+1
533159
>>> 533159/g
2551.0   ====>d
>>> 533159%326040   ====>newD % oldD
207119
>>> 533159%118921
57475
>>> 207119%g
0
>>> 207119%p
0

