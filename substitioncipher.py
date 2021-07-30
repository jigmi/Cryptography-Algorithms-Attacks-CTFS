def key(n):
    key = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cnt = 0
    for letters in alphabet:
        key[letters] = alphabet[(cnt+n) % 26]
        cnt += 1
    print(key)
    return key
def encryptor():
    message = input("Please type a message that you want to be encrypted:").upper()
    cipher = ""
    for letters in message:
        if letters in key:
            cipher += key[letters]
        else:
            cipher += letters
    print(cipher)
    return cipher
def decryptor():
    decryptor_key = {}
    decrypted_message = ""
    for letters in key:
        decryptor_key[key[letters]] = letters
    for values in cipher:
        if values in decryptor_key:
            decrypted_message += decryptor_key[values]
        else:
            decrypted_message += values
    decrypted_message = decrypted_message.lower()
    return decrypted_message
key = key(3)
cipher = encryptor()
decryptor()
