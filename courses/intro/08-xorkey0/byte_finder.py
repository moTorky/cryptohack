"""
I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
"""
from pwn import xor

f="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
b_f=bytes.fromhex(f)

for i in range(1,256):
	# if "crypto" in xor(b_f,i).decode("utf-8"):
	print(xor(b_f,i))

"""
in exc use:
└─$ python3 byte_finder.py | grep "crypto"
b'crypto{0x10_15_my_f4v0ur173_by7e}'
---
but we wanna print flag without grep it
"""
encoded = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

def decode(s):
    return ''.join([chr(s ^ a) for a in encoded])

for i in range(0, 127):
    if "crypto" in decode(i):
        print(decode(i))
"""
or:
from pwn import xor

flagBytes = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
byte=0x00

for i in range(256):
    flag=xor(flagBytes, byte).decode("utf-8")
    if("crypto" in flag):
        print(flag)
        break;
    byte=byte + 0x01
"""

"""
we know that flag start with 'c' so we xor str[0] and ord(c) and we get the magic byte :)
"""
input_str = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

key = input_str[0] ^ ord('c')
print(''.join(chr(c ^ key) for c in input_str))


