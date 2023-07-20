https://leimao.github.io/article/RSA-Algorithm/

RSA relies on the difficulty of the factorisation of the modulus N. If the primes can be found then we can calculate the Euler totient of N and thus decrypt the ciphertext.

Given N = p*q and two primes:

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

What is the totient of N? 
totient of N = φ(n)
			 =φ(pq)
			 =φ(p)φ(q)
			 =(p−1)(q−1)
			 =857504083339712752489993810776 * 1029224947942998075080348647218
			 =882564595536224140639625987657529300394956519977044270821168