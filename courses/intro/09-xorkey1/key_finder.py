"""
forma="crypto{"
for i in range(7):
...     print("".join(chr(ord(forma[i]) ^ input_str2[i])),end="")
... 
myXORke

know we have first 8 bytes of the key, letus xor "myXORkey"
"""
from pwn import xor
input_str2=bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

# for i in range(8,127):
# 	print(input_str2[i])
key="myXORkey"
print(xor(input_str2,key))