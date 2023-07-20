selecting two large primes at random: p, q 
computing their system modulus n=p.q
note ø(n)=(p-1)(q-1) 
selecting at random the encryption key e
where 1<e<ø(n), gcd(e,ø(n))=1 
solve following equation to find decryption key d 
e.d=1 mod ø(n) and 0≤d≤n 
publish their public encryption key: PU={e,n} 
keep secret private decryption key: PR={d,n}
C=M^e mod n 
M=C^d mod n 


p = 857504083339712752489993810777
q = 1029224947942998075080348647219

and the exponent:

e = 65537

What is the private key d?


>>> p = 857504083339712752489993810777
>>> q = 1029224947942998075080348647219
>>> e = 65537
>>> Qn=(p-1)*(q-1)
>>> Qn
882564595536224140639625987657529300394956519977044270821168
>>> math.gcd(e,Qn)
1
>>> n=p*q
>>> for i in range(1,n):
...     if (i*e)%Qn == 1 :
...             print(i)
...             break
====> but a for loop can work for small values of p, q, and e. However, for larger values, this approach becomes computationally inefficient 
and impractical.
so we use pow(e,-1,Qn)
>>> d = pow(e, -1, Qn)
>>> d
121832886702415731577073962957377780195510499965398469843281
-----
from Crypto.Util.number import inverse
phi = (p - 1) * (q - 1)

d = inverse(e, phi) # d = e^(-1) MOD phi

------
if u don't have e in first palse use:
import random
import math

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

# Calculate Qn
Qn = (p-1) * (q-1)

# Generate a suitable value of e
while True:
    e = random.randrange(1, Qn)
    if math.gcd(e, Qn) == 1:
        break

print("Public exponent e:", e)
