def key(n):
    key = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cnt = 0
    for letters in alphabet:
        key[letters] = alphabet[(cnt+n) % len(alphabet)]
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
# Attack commencing below by Eve, Eve only knows the cipher "QHYHU" and nothing about the above code and wants to break it. He guesses it involves the Caesar cipher so he commences attack
def key(n):
    key = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cnt = 0
    for letters in alphabet:
        key[letters] = alphabet[(cnt+n) % 26]
        cnt += 1
    return key
def decryptor(key,cipher):
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
for i in range(24):
    dkey = key(i)
    message = decryptor(dkey,"QHYHU")
    print(message)
   # Thus, the when i = 3, dkey = key(3), the output is never which is the right decrypted ciphertext.

