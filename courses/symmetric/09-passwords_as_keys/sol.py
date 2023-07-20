"""
It is essential that keys in symmetric-key algorithms are random bytes, 
#instead of passwords or other predictable data. 
The random bytes should be generated using a cryptographically-secure pseudorandom number generator (CSPRNG). If the keys are predictable in any way,
 then the security level of the cipher is reduced and it may be possible for an attacker who gets access to the ciphertext to decrypt it.

Just because a key looks like it is formed of random bytes, does not mean that it necessarily is. 
In this case the key has been derived from a simple password using a hashing function, which makes the ciphertext crackable.

"""
import hashlib
import requests

def generate_all_posibale_keys():
	f2=open('./keys','w')
	with open('./words') as f:
		for line in f:
		# For Python3, use print(line)
			line=line.strip()
			f2.write(hashlib.md5(line.encode()).hexdigest()+"\n")



# generate_all_posibale_keys()

# ciphertext_response=requests.get("https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/")
# ciphertext=ciphertext_response.json()['ciphertext']
cipher_text="c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
def fuzz_all_posibale_keys():#get flag from send request to cryptohack API
	f2=open('./keys','w')
	with open('./words') as f:
		for line in f:
		# For Python3, use print(line)
			line=line.strip()
			md5=hashlib.md5(line.encode()).hexdigest()
			try:
				response=requests.get("https://aes.cryptohack.org/passwords_as_keys/decrypt/"+ciphertext+"/"+md5+"/")
				if response.status_code == 200:
					plan=bytes.fromhex(response.json()['plaintext'])
					if "crypto".encode() in plan:
						print("flage: {0} found when using: {1} that have md5:{2}".format(plan,line,md5))
			except Exception as e:
				print(e)


# fuzz_all_posibale_keys()

from Crypto.Cipher import AES
import binascii

def decrypt(ciphertext,key):
    ciphertext = bytes.fromhex(ciphertext)
    KEY = bytes.fromhex(key)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}

def get_flag_local():
	f2=open('./keys','w')
	with open('./words') as f:
		for line in f:
		# For Python3, use print(line)
			line=line.strip()
			md5=hashlib.md5(line.encode()).hexdigest()
			try:
				ciphertext = bytes.fromhex(cipher_text)
				# KEY = hashlib.md5(line.encode()).hexdigest()
				KEY = bytes.fromhex(md5)
				cipher = AES.new(KEY, AES.MODE_ECB)
				decrypted = cipher.decrypt(ciphertext)
				plan=binascii.unhexlify(decrypted.hex())
				# if plan.startswith('crypto{'.encode()):
				#if b'crypto' in decrypted:
				if 'crypto'.encode() in plan:
					print("flage: {0} found when using: {1} that have md5:{2}".format(plan,line,md5))
					print('crypto'.encode() in bytes.fromhex(decrypted.hex()))
			except Exception as e:
				continue
				# print(e)

get_flag_local()