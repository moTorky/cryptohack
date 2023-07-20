import requests

offset='41'*15

response=requests.get("https://aes.cryptohack.org/ecb_oracle/encrypt/414141414141414141414141414141/")
target=response.json()['ciphertext'][0:32]

for i in range(1,255):
	#y = "even" if x % 2 == 0 else "odd"
	byte='0'+hex(i)[2:] if len(hex(i)[2:]) == 1 else hex(i)[2:]
	payload=offset+byte
	print("connext to: https://aes.cryptohack.org/ecb_oracle/encrypt/"+payload+"/")
	response = requests.get("https://aes.cryptohack.org/ecb_oracle/encrypt/"+payload+"/")

	if response.status_code == 200 :
		print("connected")
		t=response.json()['ciphertext'][0:32]
		print("{1} : {2}",payload,response.json()['ciphertext'])

		if target == t:
			byte='0'+hex(i)[2:] if len(hex(i)[2:]) == 1 else hex(i)[2:]
			print("first Byte :",end="")
			print(bytes.fromhex(byte))
			break