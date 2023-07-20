"""
When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters.
Hexadecimal can be used in such a way to represent ASCII strings. 
First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). 
Then the decimal numbers are converted to base-16 numbers
"""

hx="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(hx))

"""
The .hex() instance method can be called on byte strings to get the hex representation.
"""

