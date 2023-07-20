"""
in RSA or any encryption algo we need to represent strings as number in order to do the math
so we 	1. take the ord for chars to ascii number
		2. convert ascii numbers to hex 
		3. interpreted as a base-16/hexadecimal number
		4. represented in base-10/decimal.
		ex:
			message: HELLO
			ascii bytes: [72, 69, 76, 76, 79]
			hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
			base-16: 0x48454c4c4f
			base-10: 310400273487 
"""

from Crypto.Util.number import *
big_int=11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(big_int))