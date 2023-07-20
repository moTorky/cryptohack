"""
a^(p-1) ≡ 1 mod p
What is the inverse element: 3 * d ≡ 1 mod 13 ?

so d = pow(3,11)
then take mod p
d = pow(3,11)%13 = 9 


prov:
a^(p-1) ≡ 1 mod p

a^(p-1) * a^-1 ≡ 1*a^-1 mod p
a^(p-2) * a * a^-1 ≡ a^-1 mod p
a^(p-2) * 1 ≡ a^-1 mod p
a^(-1) = a^(p-2) mod p
d= a^(p-2) mod p
d= pow(3,11)%13 = 9

or:
 d = pow(3,11)
pow(3,3)=27 = 1 [13] 	=>(1) 
 11=3*3+2  				=>(2) 

so d = pow(3,11) = 3²*pow(pow(3,3),3) =>from 1
= 3²*pow(1,3) by (1)
=3²*1 =9



"""