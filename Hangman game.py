import random#importing the 'random' module for word selection
word = ["Apple", "Mango", "Window", "Book", "Eraser"]#Create list word and items are assigned
words = random.choice(word).lower()#A random word is assigned to variable words
len1 = len(words)
guessed = ["_"] * len1# Create a list of underscores for the hidden word
print("Welcome to Hangman game")
print("Guess the word:", " ".join(guessed))
chance = 6#maximum chances used to find the word
while chance != 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()#Getting a letter from user as input and converting it to lowercase
    if guess in words:#Checking whether the word found 
        print("Correct!")
        for i in range(len1):#for loop runs for length of the "words"
            if words[i] == guess:#checks whether the guess is equal to letter in word
                guessed[i] = guess#if found the underscore for the letter will be replaced 
        print(" ".join(guessed))
    else:
        chance -= 1#for each wrong guess a chance will be deducted
        print("Wrong! Chances left:", chance)
        print(" ".join(guessed))

if(chance==0 and '_' in guessed):#if the player failed to chose the word 'if' part will be executed 
    print("You lost. The word was:", words)
else:#else the player will be announced as he won
    print("You win! The word is:", words)
