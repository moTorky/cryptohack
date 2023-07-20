"""
Base64 allows us to represent binary data as an ASCII string using an alphabet of 64 characters.
 One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.
"""
import base64

hx="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
hx=bytes.fromhex(hx)
# print(hx)
print(base64.b64encode(hx[1:]))