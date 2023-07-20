"""
algo explanation:
http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
"""

def egcd(q,p):
	t1=0
	t2=1
	if q>p:
		a=q
		b=p
	else:
		a=p
		b=q
	while b != 0:
		r=a%b
		q=(a//b)
		t=t1-(t2*q)
		a=b
		b=r
		t1=t2
		t2=t
	return t1,a
# print(egcd(15,26))
t1,t=egcd(26513,  32321)
# t2=((t1*26513)-1 )// 32321
print("{0} , -{1}".format(t1,((t1*26513)-t )// 32321))

def egcd_gpt(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd_gpt(b % a, a)
        return (gcd, y - (b // a) * x, x)

print(egcd_gpt(32321,26513))
