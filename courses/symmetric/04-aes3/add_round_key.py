from pwn import *

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    text=""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            text+=(chr(matrix[i][j]))
    return text 

def add_round_key(s, k):
    # c=s.copy()
    # for i in range(len(s)):
    #     for j in range(len(k[0])):
    #         c[i][j] = s[i][j] ^ k[i][j]
    # return matrix2bytes(c)
    #or
    # return xor(s,k)
    #or
    str_list=[s[i][j] ^ k[i][j] for i in range(0,4) for j in range(0,4)]
    return "".join(chr(q) for q in str_list)

print(add_round_key(state, round_key))

