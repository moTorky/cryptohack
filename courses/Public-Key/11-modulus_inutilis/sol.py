we do see that e = 3
so we can just use ct ** (1/3) to get m 
but In Python, x ** (1/n) will give you the nth root of x for integer values of n. However, 
it may not work correctly for non-integer values of n, and may also produce rounding errors due to floating-point arithmetic. 
In addition, it may not give exact results for large integer values of x and n, as Python's built-in integers have a fixed size.

To get precise results for large integers, it's better to use a specialized library like gmpy2 or mpmath. 
These libraries are designed to handle large integers with high precision and accuracy, and provide functions like iroot that are specifically 
designed for computing integer roots.

>>> from gmpy2 import iroot
>>> iroot(ct,3)
(mpz(624239975241694158443315202759206900318542905782320965248893), True)
>>> iroot(ct,3)[0]
mpz(624239975241694158443315202759206900318542905782320965248893)
>>> iroot(ct,3)[0][2:]
mpz(156059993810423539610828800689801725079635726445580241312223)
>>> long_to_bytes(624239975241694158443315202759206900318542905782320965248893)
b'crypto{N33d_m04R_p4dd1ng}'


#using binary search
def find_cube_root(n):
       low = 0
       high = n
       while low < high:
           mid = (low+high)//2
           if mid**3 < n:
               low = mid+1
           else:
               high = mid
       return(low)

ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957

print(long_to_bytes(find_cube_root(ct)))