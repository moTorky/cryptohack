from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
KEY = ?
FLAG = ?
@chal.route('/ecb_oracle/encrypt/<plaintext>/')
def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return {"ciphertext": encrypted.hex()}

'''
we only have this encrypt function that take hexinput and return hex output
the pad() function adds padding bytes to the plaintext to ensure that its length is a multiple of the block size, 
and the FLAG.encode() method converts the FLAG string to bytes so it can be concatenated with the plaintext before padding.
-----
how to get flag from that ?--> byte-at-a-time attack 
-----
1.Choose a known plaintext prefix: The attacker selects a known plaintext prefix, such as "A" or "password=". 
This prefix will be used in all of the plaintexts that are encrypted during the attack.

2.Determine the length of the secret plaintext: The attacker determines the length of the secret plaintext by encrypting different-length 
plaintexts with the chosen prefix and analyzing the resulting ciphertexts. The length of the secret plaintext can be inferred from the length of 
the ciphertexts.

3.Determine the secret plaintext one byte at a time: Starting with the first byte of the secret plaintext, 
the attacker constructs a series of plaintexts that have the chosen prefix plus one additional byte. For example, 
if the chosen prefix is "password=" and the first byte of the secret plaintext is "h", the attacker would encrypt the plaintexts 
"password=a", "password=b", "password=c", and so on, until the correct byte of the secret plaintext is found. 
This is repeated for each byte of the secret plaintext until the entire plaintext is recovered.

4.Repeat the process for other blocks (if applicable): If the secret plaintext is longer than one block (16 bytes for AES in ECB mode),
    the attacker can repeat the byte-at-a-time attack for each block until the entire plaintext is recovered.
-----    
https://zachgrace.com/posts/attacking-ecb/    
-----
proccess
1. choose pattern =>414141414141  or A*6
2. get flag length
    input:414141414141  output:                                bf65fb34f51bf9b8acbdb3ed28678362779f56d8fb3019c4a1e2cb0b74281657
                                                               8750d901af619c2fcda599eab2ae9f2a779f56d8fb3019c4a1e2cb0b74281657
                                                               60ae53755e7425a5c93804ac600fc5b1779f56d8fb3019c4a1e2cb0b74281657         
                                                               09d0fc798844f8506cf703aed06969862569d0e83489b016fc743263caa0b7d8
                                                               c7fe0794763a7cc0db166d18fd24f11d2569d0e83489b016fc743263caa0b7d8
                                                               9cb05ea1ee8a77627cbed8e345f6df4b779f56d8fb3019c4a1e2cb0b74281657
    input:41414141414141outout:08caf81d9fc5ebdd1cad5e8701d7cf5ebed812700886882eade550f0f73192f267f7b4ed431d69a986c4e8a7fb810c97
                               318bf9bdfe477f6b0ef1378b996212cbbf65fb34f51bf9b8acbdb3ed28678362779f56d8fb3019c4a1e2cb0b74281657

    so the lengh of the flag is:26 Byte  as input:6B out:32B (6+26)  , input:7B out:48B (7+26+15)

3.letus prove that the plaintext are put in the front and get offset
input:output
41414141414141414141414141414141:318bf9bdfe477f6b0ef1378b996212cb c629f8744a2c1fa153f90bf2e0911b32 50673f6844d0ace711e35abde39252a7
4141414141414141414141414141414141414141414141414141414141414141:
318bf9bdfe477f6b0ef1378b996212cb 318bf9bdfe477f6b0ef1378b996212cb c629f8744a2c1fa153f90bf2e0911b32 50673f6844d0ace711e35abde39252a7

4. now we gonna send blocksize-1 as input in order to encrypt one Byte from the secret flag like
414141414141414141414141414141:88357563133f281448ccddb2716b463e 07c621d4ed9af3acc103bdb3bb81fc75 f2bb614792d17621b7c528e82eb1564a
                               318bf9bdfe477f6b0ef1378b996212cb 1fa315727cb28ec0b338d323192acaa8 2569d0e83489b016fc743263caa0b7d8
then letus brute force this Byte by send 
4141414141414141414141414141414101
...................
4141414141414141414141414141414163
useing first_byte.py
connect to: https://aes.cryptohack.org/ecb_oracle/encrypt/41414141414141414141414141414163/
connected
41414141414141414141414141414163:88357563133f281448ccddb2716b463ec629f8744a2c1fa153f90bf2e0911b3250673f6844d0ace711e35abde39252a7
first Byte :b'c'

wow now letus get the all 26 bytes => get_flag.py

and we get it:
b'crypto{p3n6u1n5_h473_3cb'
63727970746f7b70336e3675316e355f683437335f336362
connect to:https://aes.cryptohack.org/ecb_oracle/encrypt/41414141414141/
target :08caf81d9fc5ebdd1cad5e8701d7cf5ebed812700886882eade550f0f73192f2
offset :4141414141414163727970746f7b70336e3675316e355f683437335f336362
b'crypto{p3n6u1n5_h473_3cb}'
========================> that's take about half hour 
41414141414141414141414141414141414141414141414141414141414141:
318bf9bdfe477f6b0ef1378b996212cb88357563133f281448ccddb2716b463e07c621d4ed9af3acc103bdb3bb81fc75f2bb614792d17621b7c528e82eb1564a
4141414141414141414141414141414141414141414141414141414141414163:
318bf9bdfe477f6b0ef1378b996212cb88357563133f281448ccddb2716b463ec629f8744a2c1fa153f90bf2e0911b3250673f6844d0ace711e35abde39252a7
414141414141414141414141414141414141414141414141414141414141:
318bf9bdfe477f6b0ef1378b996212cb0c332297343b5e9b866550b433b0bd6e99206560ad303309542faf4b8fe2f5c12d91f9e4a7e606c05cce010a539b0675
4141414141414141414141414141414141414141414141414141414141416372:
318bf9bdfe477f6b0ef1378b996212cb0c332297343b5e9b866550b433b0bd6ec629f8744a2c1fa153f90bf2e0911b3250673f6844d0ace711e35abde39252a7
4141414141414141414141414141414141414141414141414141414141:
318bf9bdfe477f6b0ef1378b996212cbfd0f0d1aad37310cf176b9b01dc54ea11e4ad7c3344c39e34ce60dc1c8688f601eef8877895b3a8f3ccaad2481e70337
4141414141414141414141414141414141414141414141414141414141637279
318bf9bdfe477f6b0ef1378b996212cbfd0f0d1aad37310cf176b9b01dc54ea1c629f8744a2c1fa153f90bf2e0911b3250673f6844d0ace711e35abde39252a7
'''
