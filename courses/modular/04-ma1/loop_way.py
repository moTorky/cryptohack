a=273246787654
p_1=65536
p=65537

while p_1>0:
	a=(a%p*a%p)%p
	p_1-=1
print(a) #output 1


"""---------
we see p=p_1+1
we have a fermat's little theorem that say if ===> a^(p-1) ≡ 1 mod p 
if 	1. p is prim number 
	2. a is a positive integer not divisible by p => gcd(a,p)=1


we do have the 2 condetions so the out is 1

anther ex is p=5, a=2
a^(p-1) ≡ 1 mod p 
2^(5-1) ≡ 1 % 5
2^4 ≡ 1 mod 5
16 ≡ 1 mod 5                  => true remender for 16/5 is 1
16%5 = 1 
see https://youtu.be/3Cb0ys-jppU
-------------------

we also can revert it => see next Q mdiv
What is the inverse element: 3 * d ≡ 1 mod 13 ?

so d = pow(3,11)
then take mod p
d = pow(3,11)%13 = 9 
"""