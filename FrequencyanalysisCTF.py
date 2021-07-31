#Cipher uses substition algorithm and thus, is prone to frequency analysis which will be implemented below.
ciphertext = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""
letter_freq = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
               'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
               'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
               's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
               'y': 0.0197, 'z': 0.0007}
cipher_frequency = {}
v = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
plain_chars_left = "abcdefghijklmnopqrstuvwxyz"
def frequency_analysis():
    global cipher_frequency
    for letters in alphabet:
        cipher_frequency[letters] = 0
        letter_count = 0
    for rubish in ciphertext:
        if rubish in cipher_frequency:
            cipher_frequency[rubish] += 1
            letter_count += 1
    analysis = {}
    for c in cipher_frequency:
        cipher_frequency[c] = round(cipher_frequency[c]/letter_count,4)    
        for values in letter_freq:
            analysis.setdefault(c,[]).append((values,abs(round((cipher_frequency[c]-letter_freq[values]),4))))
            analysis[c].sort(key = lambda x:x[1])
    return analysis
def mapping():
    global plain_chars_left
    global v
    for cipher_chars_left in alphabet:
        for plain_char,diff in frequency_analysis[cipher_chars_left]:
            if plain_char in plain_chars_left:
                v[cipher_chars_left] = plain_char
                plain_chars_left = plain_chars_left.replace(plain_char,"")
                break
    print(f'current mappings are{v}')
    decrypted_cipher_text = ""
    for uncoded in ciphertext:
        if uncoded in v:
            decrypted_cipher_text += v[uncoded]
        else:
            decrypted_cipher_text += uncoded
    print(f"Generated text is \n{decrypted_cipher_text}")
def change_mappings(ciphertext,mappings):
    global v
    x = 0
    for letters in v:
        if x == 1:
            break
        else:
            for oo in v[letters]:
                if mappings == oo:
                    v[letters] = v[ciphertext]
                    v[ciphertext] = mappings
                    mapping()
                    x += 1
                    break
                else:
                    pass
frequency_analysis = frequency_analysis()
choice = input("Would you like to be displayed the frequency of the ciphertext letters to the possible real characters?")
if choice == "yes":
    for orientation in frequency_analysis:
        print(orientation)
        print(frequency_analysis[orientation])
else:
    print("continuing on")
mapping()
change_mappings("v","c")
change_mappings("m","a")
change_mappings("p","h")
change_mappings("w","i")
change_mappings("s","p")
change_mappings("u","r")
change_mappings("k","n")
change_mappings("h","l")
change_mappings("o","g")
change_mappings("a","x")
change_mappings("r","e")
change_mappings("g","s")
change_mappings("i","s")
change_mappings("c","w")
change_mappings("q","d")
change_mappings("d","d")
change_mappings("f","q")
change_mappings("e","v")
change_mappings("q","k")
change_mappings("g","s")
change_mappings("i","s")
change_mappings("y","m")
change_mappings("t","y")
 #Decrypted Cipher is below
''' because the practice of the basic movements of kata is
the focus and mastery of self is the essence of
matsubayashi ryu karate do i shall try to elucidate the
movements of the kata according to my interpretation
based on forty years of study
  it is not an easy task to explain each movement and its
significance and some must remain unexplained to give a
complete explanation one would have to be qualified and
inspired to such an extent that he could reach the state
of enlightened mind capable of recognijing soundless
sound and shapeless shape i do not deem myself the final
authority but my experience with kata has left no doubt
that the following is the proper application and
interpretation i offer my theories in the hope that the
essence of okinawan karate will remain intact '''

