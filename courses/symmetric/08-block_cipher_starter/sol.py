#we need to encrypt messages much longer than a single block. A mode of operation describes how to use a cipher like AES on longer messages.
#All modes have serious weaknesses when used incorrectly.
#from Crypto.Cipher import AES


#KEY = ?
#FLAG = ?


#@chal.route('/block_cipher_starter/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}

#@chal.route('/block_cipher_starter/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}

#the above is the internale implamet and route
#so we need to use requests module to connect to API and ge data
import requests

response = requests.get("http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/")
print(response.json())
ciphertext = response.json()['ciphertext']
response = requests.get("http://aes.cryptohack.org/block_cipher_starter/decrypt/" + ciphertext)
print(response.json())
print(bytes.fromhex(response.json()['plaintext']).decode('utf-8'))
