# Sharmada Iyer - Assignment 2 - Python Programming - Dr. Oge Marques - Summer 2021


The Caesar Cipher encrypt and decrypt was an interesting algorithm to implement. This assignment was a eye-opener as I learned a lot of python syntax and it was also a problem to solve.

# How I implemented the algorithm

Firstly, I tried to create a while loop that only ends when the user wants to quit the program. If this does not go first, it would very hard to format in the end. From there I want to get a user's input. All my inputs with the exception of the key input has an else statement in which if an incorrect input is placed, it will ask the user if they want to start over from the beginning. The key input was quite difficult to make a conditional statement with because the input was defaulted to a string instead of an integer. Therefore it was quite difficult to write a conditional statement for anything outside of an integer. 

The Cipher portion of the assignment was quite challenging but very simple at the end. The idea for encryption is to get the index by subtracting the ASCII value with the ASCII value of uppercase or lowercase 'A' respectufully. This can be used to add on the shift number that was input by the user and find the remainder of the result by modding it by 26. For example, if the letter 'Z' was a letter in the input and we want to shift it by 3, the equation would be the following.
## new index = ((090-065)+3) % 26 = 28- % 26 = 2

We will add this 25 to the ASCII value of uppercase 'A' to get the ASCII value of the new shifted value and then convert it to the letter which is 'C'.

The same process can be done for decryption except we are subtracting the original index by the shifted value. 

Note that the key value will work with a negative value as well. 

With the exception of incorrect key value entry, when the program approaches the end, the user will be asked if they want to try again. If they insert anything other than Y,y,n or N, the program will terminate.  