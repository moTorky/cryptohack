"""
For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100. We can XOR integers by first converting the integer from decimal to binary. 
We can XOR strings by first converting each character to the integer representing the Unicode character.

challenge:
Given the string label, XOR each character with the integer 13. 
Convert these integers back to a string and submit the flag as crypto{new_string}.
"""

# from operator import xor
# print(xor(int("l"),1))

sd="label"
print("crypto{",end="")
print("".join(chr(ord(o)^13) for o in sd),end="}")