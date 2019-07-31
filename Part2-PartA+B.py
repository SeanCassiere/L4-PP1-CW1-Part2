# Encoding & Decoding
choice=True
# Cipher Function
def cipherfunc(wordx,key):
    charset="abcdefghijklmnopqrstuvwxyz"
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
print("In this program you can choose to encode and/or decode a string of your choice.")
while choice==True: # Decision Loop/Prompt
    decision=str(input("Options:\n\t e for encoding.\n\t d for decoding.\n\t q to quit.\nChoose your option: "))
    if decision.lower()=="e":
        word=str(input("Enter your message to be encoded: \n"))
        while choice==True:
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
    elif decision.lower()=="d":
        word=str(input("Enter your already encoded message to be decoded: \n"))
        while choice==True:
            try:
                key=int(input("Enter the key used to encode the message\nRange 1-25: "))
            except:
                print("Your key need to be an integer value, eg. 1, 3, 5\n")
                continue
            if key>=1 and key<=25:
                print("Decoded message:",cipherfunc(word,-key),"\n")
                break
            else:
                print("Key is not in range of 1-25.\nTry again.")
    elif decision.lower()=="q":
        print("Quiting")
        choice=False
    else:
        print("Sorry that response is not recognised.\n")
