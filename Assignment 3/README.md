# Sharmada Iyer - Assignment 3 - Python Programming - Dr. Oge Marques - Summer 2021

This assignment had similar logistics to Assignment 2. In this Assignment, I have modified the code by a lot. The logic for the Caesar Cipher remains the same hence it will not be explained again.

First is the files! When reading the files, I knew that I was going to have to rename the file for later so I had the user input simply the name of the file without the extension. This way, the user doesn't have to go through the hassle of type 4 extra character and also at the end of the program, the file name can be modified to the output file much easily

Other than the output file, the user only has to input whether they would like to encrypt or decrypt the file. If they answer any other value, an error message will pop up. The key is hardcoded to 3. 

For the implementation of this assignment, i needed to operate at a word level, which was tricky. An initial loop that runs through the beginning to end of the file. I also created a loop that detected letters, if they were letters, the were appended to the end of a empty string called word. As soon as the loop arrives at a character that is not alphabetical, an encryption/decryption function is implemented depending on the letter the user chose. Both functions have word and key as parameters, detect every letter whether they are uppercase or lowercase, and return the resulting Caesar Cipher at the end. once so, the word is appended to a variable that gathers all the words being encrypted and the character that is not alphabetical is added to the end before continuing. The word variable at each loop.

once finished, an output file is created and "_enc.txt" and "dec.txt" is inserted at the user input file name depending on whether they encrypted or decrypted the contents of the file. 

Finally, the files are closed and the users are asked whether if they would like to try again. 