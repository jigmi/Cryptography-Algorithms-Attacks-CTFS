def key():
  key = {}
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for letters in alphabet:
    generator = random.choice(alphabet)
    key[letters] = generator
    alphabet = alphabet.replace(generator,"")
   return key
def encrypt(key,message):
  ciphertext = ""
  for letters in message:
    if letters in key:
      ciphertext += key[letters]
     else:
      ciphertext += letters
  return ciphertext
def decrypt(ciphertext):
  
  
      
   
  
  
