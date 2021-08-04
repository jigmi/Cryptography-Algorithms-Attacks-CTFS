from random import randint
import secrets
def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True
def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p
def is_generator(g,p):
    for i in range(1,p-1):
        if (g**i) % p == 1:
            return False
    return True
def get_generator(p):
    for g in range(2,p):
        if is_generator(g,p):
            return g
p=generate_big_prime(14)
g = get_generator(p)
print(g,p)
#this will be sent unecnrypted to the other party.
#Alice
a = secrets.randbelow(100000000)
ga = pow(g,a,p) #(g**a)%p sent into public to Bob
#Bob
b = secrets.randbelow(100000000)
gb = pow(g,b,p) #sent into public o alice
#Alice with Bob's g_and_b 
gba = pow(gb,a,p)
#Bob with Alice's g_and_a
gab = pow(ga,b,p)  
print(gba,"alice")
print(gab,"Bob")
hashA= hashlib.sha256(str(gba).encode("utf-8")).digest() 
