###########################################################################
### COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###            Assignment 2: Basic Cryptography App (in Python!)        ###
###              Sharmada Iyer - Z23479365                              ###
###########################################################################


print("--------> Welcome to the Caesar Cipher App! <--------\n\n\n")
print("Instructions: When prompted, enter a phrase,key, and the operation of your choice.")
print("The key is the number of positions further in the alphabet you would like to move. ")
print("Choose E to Encrypt the message or D to Decrypt the message.\n\n")
print("Let's begin!\n\n\n\n")

userQuit = "Y"



while userQuit == "Y" or userQuit == "y":
    newphrase = ""
    phrase = input("Input a phrase of your choice: ")

    if phrase.isalpha():
        key = int(input("Enter a key: "))
        ED = input("Encrypt or Decrypt(E/D): ")
        ED = ED.lower()
        if ED == "e":
            for c in phrase:
                if c.isupper():
                    index = ord(c)-ord("A")
                    nindex = (index+key) % 26
                    unicode = nindex + ord("A")
                    newlet = chr(unicode)
                    newphrase = newphrase+newlet

                else:
                    index = ord(c)-ord("a")
                    nindex = (index+key) % 26
                    unicode = nindex + ord("a")
                    newlet = chr(unicode)
                    newphrase = newphrase+newlet

                    
            print("\n\n\n")
            print("The encrypted word version is: " + newphrase)

        elif ED =="d":
            for c in phrase:
                if c.isupper():
                    index = ord(c)-ord("A")
                    nindex = (index-key) % 26
                    unicode = nindex + ord("A")
                    newlet = chr(unicode)
                    newphrase = newphrase+newlet

                else:
                    index = ord(c)-ord("a")
                    nindex = (index-key) % 26
                    unicode = nindex + ord("a")
                    newlet = chr(unicode)
                    newphrase = newphrase+newlet
            
            print("\n\n\n")
            print("The decrypted word version is: " + newphrase)
        else:
            print("Invalid character")

    else:
        print("The phrase has an unknown character.")

    userQuit = input("Would you like to try again? (Y/N): ")
