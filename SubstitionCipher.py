import random
def key():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    for letters in alphabet:
        generator = random.choice(alphabet)
        key[letters] = generator
        alphabet = alphabet.replace(generator,"")
    return key
def encrypt(key,message):
    message = message.upper()
    ciphertext = ""
    for letters in message:
        if letters in key:
            ciphertext += key[letters]
        else:
            ciphertext += letters
    return ciphertext
def decrypt(ciphertext):
    decrypted_message = ""
    for letters in ciphertext:
        for values in alphabet:
            if letters in key[values]:              
                decrypted_message += values
            else:
                pass
    return decrypted_message
key = key()
print(key)
ciphertext = encrypt(key,"I love pikachu but i also like charizard")
plain_text = decrypt(ciphertext).lower()
print(plain_text)
#Attack commencing below by Eve. 

  
      
   
  
  
