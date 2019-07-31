# Encoding Only
choice_key=True
# Cipher Function
def cipherfunc(wordx,key):
    charset="abcdefghijklmnopqrstuvwxyz" #abcdefghijklmnopqrstuvwxyz
    new_word=""
    for baseCharacter in range(len(wordx)):
        if wordx[baseCharacter]==" ": # Check for ' ' space
            new_word+=" "
        else: #Standard alphabetical shifting
            for cipherPosition in range(26):
                if wordx[baseCharacter]==charset[cipherPosition]:
                    new_word+=charset[(cipherPosition+key)%26]
                elif wordx[baseCharacter].istitle()==True: # Uppercase char skip
                    new_word+=wordx[baseCharacter]
                    break
                elif wordx[baseCharacter] not in charset: # All undefined charset chars
                    new_word+=wordx[baseCharacter]
                    break
    return new_word
# Program Info message
print("In this program you can encode and decode a string of your choice.")
word=str(input("Enter your message to be encoded: \n"))
while choice_key==True:
    try:
        key=int(input("Enter the key to encode the message.\nRange 1-25: "))
    except:
        print("Your key need needs to be an integer value, eg. 1, 3, 5\n")
        continue
    if key>=1 and key<=25:
        print("Encoded message:",cipherfunc(word,key),"\n")
        break
    else:
        print("Key is not in range of 1-25.\nTry again.")
