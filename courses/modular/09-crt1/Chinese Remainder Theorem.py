The Chinese Remainder Theorem gives a unique solution to a set of linear congruences if their moduli are coprime.

This means, that given a set of arbitrary integers ai, and pairwise coprime integers ni, such that the 
following linear congruences hold:

x ≡ a1 mod m1
x ≡ a2 mod m2
...
x ≡ an mod mn

Note "pairwise coprime integers" means that if we have a set of integers {m1, m2, ..., mi}, 
all pairs of integers selected from the set are coprime: gcd(mi, mj) = 1.

There is a unique solution x ≡ a mod M where M = m1 * m2 * ... * mn.

x=(a1M1N1 + a2M2N2 + anMnNn) mod M
where Nn is inverse of Mn 
and M=m1*m2*....mn
M1 = M/m1
Mn = M/Mn
M1*N1=1 mod m1 
Mn*Nn=1 mod mn 
#a^(p-1) ≡ 1 mod p
#d=a^(p-2) mod p

In cryptography, we commonly use the Chinese Remainder Theorem to help us reduce a problem of very large 
integers into a set of several, easier problems.

Given the following set of linear congruences:

x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17

Find the integer a such that x ≡ a mod 935
a1=2
a2=3
a3=5
m1=5
m2=11
m3=17
M=m1*m2*m3
M1=M//m1
M2=M//m2
M3=M//m3
#M1*N1=1 mod m1 
N1=pow(M1,(m1-2),m1)
N2=pow(M2,(m2-2),m2)
N3=pow(M3,(m3-2),m3)
x=(a1*M1*N1 + a2*M2*N2 + a3*M3*N3) % M
#then we have x ≡ a mod 935 => a=x%935
x=a=872