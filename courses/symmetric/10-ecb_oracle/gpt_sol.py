import requests
import binascii


def query_api(plaintext):
    plain_hex=b'{plaintext}'.hex()
    url = f"https://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/"
    print("first url: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        ciphertext = binascii.unhexlify(response.json()["ciphertext"])
        return ciphertext
    else:
        return None


def get_block_size():
    for i in range(1, 17):
        plaintext = "A" * i * 2
        ciphertext = query_api(plaintext)
        if ciphertext:
            if ciphertext[:i] == ciphertext[i:i*2]:
                return i
    return None


def get_flag():
#    block_size = get_block_size()
    block_size = 16
    if not block_size:
        print("Error: Could not determine block size")
        return None
    print(f"Block size is {block_size}")

    flag_len = 0
    while True:
        flag_len += 1
        plaintext = "A" * flag_len * 2
        ciphertext = query_api(plaintext)
        if ciphertext:
            num_blocks = len(ciphertext) / block_size
            for i in range(num_blocks - 1, -1, -1):
                for j in range(block_size - 1, -1, -1):
                    pad_len = block_size - j - 1
                    pad = "A" * pad_len * 2
                    target = ciphertext[i*block_size:(i+1)*block_size]
                    for k in range(256):
                        guess = pad + hex(k)[2:].zfill(2)
                        if query_api(guess)[:block_size] == target:
                            break
                    else:
                        flag_len -= 1
                        break
                else:
                    continue
                break
            else:
                continue
            break
    print(f"Flag length is {flag_len}")

    flag = ""
    for i in range(flag_len):
        for j in range(block_size - 1, -1, -1):
            pad_len = block_size - j - 1
            pad = "A" * pad_len * 2
            target = ciphertext[i*block_size:(i+1)*block_size]
            for k in range(256):
                guess = pad + hex(k)[2:].zfill(2)
                if query_api(guess)[:block_size] == target:
                    flag += chr(k)
                    break
    print(f"Flag is {flag}")
    return flag


if __name__ == "__main__":
    get_flag()
