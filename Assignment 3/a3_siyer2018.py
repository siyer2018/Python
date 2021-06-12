###########################################################################
### COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###            Assignment 3:  Cryptography App using files       ###
###              Sharmada Iyer - Z23479365   DUE:6/8/21                   ###
###########################################################################

print("--------> Welcome to the Caesar Cipher App! <--------\n\n\n") #INTRODUCTION AND INSTRUCTIONS FOR USERS
print("Instructions: When prompted, enter a file name to read and the operation of your choice.")
print("The key is set to 3 positions further/backwards from the letter you would like to move from. ")
print("Choose E to Encrypt the message or D to Decrypt the message.\n\n")
print("Let's begin!\n\n\n\n")


def encrypt(word,key): #ENCRYPTION FUNCTION

    newphrase=""
    for c in word: #TRAVERSES THROUGH LETTERS OF THE PASSED PARAMETER WORD
                if c.isupper(): #UPPERCASE (CAESAR CIPHER)
                    index = ord(c)-ord("A")
                    nindex = (index+key) % 26
                    unicode = nindex + ord("A")
                    newlet = chr(unicode)
                    newphrase = newphrase+newlet

                else: #LOWERCASE (CAESAR CIPHER)
                    index = ord(c)-ord("a")
                    nindex = (index+key) % 26
                    unicode = nindex + ord("a")
                    newlet = chr(unicode)
                    newphrase = newphrase+newlet

    return newphrase #RETURNS NEW PHRASE

def decrypt(word,key): #DECRYPTION FUNCTION
    newphrase=""
    for c in word: #TRAVERSES THROUGH LETTERS OF THE PASSED PARAMETER WORD
        if c.isupper(): #UPPERCASE (CAESAR CIPHER)
            index = ord(c)-ord("A")
            nindex = (index-key) % 26
            unicode = nindex + ord("A")
            newlet = chr(unicode)
            newphrase = newphrase+newlet

        else: #LOWERCASE (CAESAR CIPHER)
            index = ord(c)-ord("a")
            nindex = (index-key) % 26
            unicode = nindex + ord("a")
            newlet = chr(unicode)
            newphrase = newphrase+newlet
    
    return newphrase

userQuit = "Y" #PRESET WHILE LOOP TO YES 
while userQuit == "Y" or userQuit == "y": #WHILE USER CONTINUES
    word = "" #DEFINES WORD
    newword="" #DEFINES NEW WORD
    
    f = input("Input a file name (without the file extension): ") #USER INPUT
    filename=f +".txt" #ADDED EXTENSION 
    print("The following is the input file name: ",filename) #PRINTED FILE NAME
    fphrase=open(filename,"r") #READING FILE


    key = 3
    ED = input("Encrypt or Decrypt(E/D): ")
    ED = ED.lower()

    for c in fphrase.read(): #TRAVERSE THROUGH CHARACTERS TILL END OF FILE
        if c.isalpha(): #IF LETTER
            word=word+c #ADD LETTER AT END OF WORD
        else: #IF OTHER CHARACTER
            if ED == 'e': #IF USER INPUT ENCRYPT
                newword=newword+encrypt(word,key)+c #ADD ENCRYPTED WORD TO ENCRYPTED PHRASE WITH THE OTHER CHARACTER
                word="" #RESET WORD
            elif ED == 'd': #IF USER INPUT DECRYPT
                newword=newword+decrypt(word,key)+c #ADD DECRYPTED WORD TO DECRYPTED PHRASE WITH THE OTHER CHARACTER
                word="" #RESET WORD
            else:
                print("Invalid Value") #PRINT INVALID VALUE
                break #BREAK LOOP

    

    if  ED == 'e': #IF USER INPUT ENCRYPT
        filename=f+"_enc.txt" #ADDED EXTENSION WITH ENC
    elif ED == 'd': #IF USER INPUT DECRYPT
        filename=f+"_dec.txt" #ADDED EXTENSION WITH DEC

    
    finalWord=open(filename,"w") #OPEN FILE TO WRITE
    finalWord.write(newword) #WRITE RESULT IN FILE

    print("The following is the result:", newword) #PRINT RESULT
    print("The following is the output file name: ",filename) #PRINT FILE NAME
    

    fphrase.close() #CLOSE READ FILE
    finalWord.close() #CLOSE WRITE FILE


    userQuit = input("Would you like to try again? (Y/N): ") #ASK USER IF TRY AGAIN


