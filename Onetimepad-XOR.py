import random
def key_stream(n):
    stream = []
    for values in range(n):
        stream.append(random.randrange(0,256))
    return stream
def encrypt(key,message):
    xor = []
    length = min(len(key),len(message))
    for values in range(length):
        xor.append(key[values]^message[values])
    xor = bytes(xor)
    return xor
def decrypt(key,ciphertext):
    plaintext = []
    length = min(len(key),len(ciphertext))
    for values in range(length):
        plaintext.append(key[values]^ciphertext[values])
    plaintext = bytes(plaintext)
    return plaintext
key = key_stream(len(message))
print(key)
message = "Hello, we are currently implementing the one time pad".encode("utf-8")
ciphertext = encrypt(key,message)
print(ciphertext)
decrypt(key,ciphertext)
