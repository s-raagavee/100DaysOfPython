#Task: Using the knowledge gained from Day 1 - 7 to create the hangman game.

import hangman_words, hangman_art, random

#print logo
print(hangman_art.logo)

#starting lives
lives = 0

#choose a random word
chosen_word = hangman_words.word_list[random.randint(0, len(hangman_words.word_list)-1)]

#To use for testing
print(f"chosen word for testing purposes: {chosen_word}\n")

#create blanks for chosen word and store in list
display = ""
for ch in range(len(chosen_word)):
    display += "_"

#save correct guessed letters in chosen_Word
correct_letters = []
for ch in display:
    correct_letters.append(ch)

#save all letters guessed
guessed_letters = []

#while loop for continuous guessing
game_over = False
while not game_over:

    print(f"Word to guess: {display}")

    #get user's guess
    guess = input("Guess a letter: ").lower()

    #make sure user input is one letter
    if len(guess) == 1:

        if guess not in guessed_letters:
            #check letters in chosen word and save in correct_letters
            pos = 0
            letters_found = 0
            for letter in chosen_word:
                if guess == letter:
                    correct_letters[pos] = guess
                    letters_found += 1
                pos += 1

            #store letter in guess letters
            guessed_letters.append(guess)
        else:
            print("\nYou have already guessed this letter! Try again!")

        #if letter does not exist in chosen word then lose a life
        if letters_found == 0:
            lives += 1

        #display letters found so far
        display = ""
        for item in correct_letters:
            display += item

        #display hangman lives
        print(hangman_art.stages[lives])
        
        #game over when user finds word
        if display == chosen_word:
            print(f"YOU WIN!\nYou found the word: {display}")
            game_over = True
        
        #game over when user runs out of lives
        if lives == 6:
            print(f"YOU LOSE!\nYou ran out of lives\n The word was {chosen_word}")
            game_over = True
    
    else:
        print("ERROR! Please input 1 letter! \n\n")