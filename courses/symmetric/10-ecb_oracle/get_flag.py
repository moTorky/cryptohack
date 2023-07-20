import requests
import time

flag=''
offset='41'*31
b_flag=''

for index in range(1,27):
	offset='41'*(31-index+1)
	print(b_flag)
	try:
		response=requests.get("https://aes.cryptohack.org/ecb_oracle/encrypt/"+offset+"/")
		target=response.json()['ciphertext'][0:64]
		print("connect to:",end="")
		print("https://aes.cryptohack.org/ecb_oracle/encrypt/"+offset+"/")
		if response.status_code==200:
			print("target :",end="")
			print(target)
			# offset+='41'*(index-1)
			offset+=b_flag
			print("offset :",end="")
			print(offset)
			for i in range(1,255):
			# for i in range(98,100):
				#y = "even" if x % 2 == 0 else "odd"
				byte='0'+hex(i)[2:] if len(hex(i)[2:]) == 1 else hex(i)[2:]
				payload=offset+byte
				# print("connext to: https://aes.cryptohack.org/ecb_oracle/encrypt/"+payload+"/")
				try:
					response = requests.get("https://aes.cryptohack.org/ecb_oracle/encrypt/"+payload+"/")
					if response.status_code == 200 :
					# print("connected")
						t=response.json()['ciphertext'][0:64]
						# print("{1} : {2}",payload,response.json()['ciphertext'])

						if target == t:
							byte='0'+hex(i)[2:] if len(hex(i)[2:]) == 1 else hex(i)[2:]
							b_flag+=byte
							flag=bytes.fromhex(b_flag)
							print(flag)
							break
				except Exception as e:
					print(e)
					i-=1
					time.sleep(1)
					continue
	except Exception as e:
		print(e)
		index-=1
		time.sleep(1)
		continue