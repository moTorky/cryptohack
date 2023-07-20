 Adrien's been looking at ways to encrypt his messages with the help of symbols and minus signs. Can you find a way to recover the flag?

>>> bin(99)
'0b1100011'
>>> bin(99)[2:].zfill(8)
'01100011'
>>> int(0b01100011)
99
>>> chr(int(0b01100011))
'c'


so what encrypt_flag do is make plaintext that have string of 0,1's , then for 0,1 it make random
number(e) between 1,p then using a,e,p we get n such that n = pow(a, e, p) 
and if the index is =1 we append that n , otherwise we append (-n%p)
where a = 288260533169915 ,p = 1007621497415251  

