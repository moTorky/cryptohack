"""
xor probrates:
	Commutative: A ⊕ B = B ⊕ A
	Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
	Identity: A ⊕ 0 = A
	Self-Inverse: A ⊕ A = 0 

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
"""

key1="a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
b_key1=bytes.fromhex(key1)
key2_xor_key1="37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
b_key2=bytes([a ^ b for a, b in zip(b_key1 , bytes.fromhex(key2_xor_key1))])
key3_xor_key2="c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
b_key3= bytes([a ^ b for a, b in zip(b_key2 , bytes.fromhex(key3_xor_key2))])

b_xor_3keys=bytes([a ^ b ^ c for a, b , c in zip(b_key1,b_key2,b_key3)])

flag = bytes([a ^ b for a , b in zip(b_xor_3keys, bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"))])

print(flag)

#enhance 
from pwn import xor
k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
print(xor(k1,k2_3,flag))  