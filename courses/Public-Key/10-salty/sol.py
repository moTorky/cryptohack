RSA equation can be resumed as c = pow(m,e) [n] 
where : - m is plaintext
        - c is ciphertext
        - n is the modulus
        - e is the public exponent

Here e is equal to 1 so m = c [n]
c < n so m = c

Here c=44981230718212183604274785925793145442655465025264554046028251311164494127485
To recover, the flag, do something like "long_to_bytes(c)" in Python with Crypto.Util.number 
from Crypto.Util.number import long_to_bytes
bytes.fromhex(hex(c)[2:])
long_to_bytes(c)