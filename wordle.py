# pip install termcolor

import random as r
from termcolor import cprint
tw = open("target_words.txt", "r")
aw = open("all_words.txt", "r")
words = aw.read().split("\n")
guess_count = 0
past_guesses = []

#get random target word function
lines = tw.readlines()
# tar_word = r.choice(lines)
# print(tar_word)
tar_word = "excel"

while True:
    #guessing mechanics
    while True:
        print("---------------")
        word = input("Enter a Guess: ").strip().lower()
        print("---------------")
        print()

        if word in words:
            guess_count += 1
            break
        else:
            print("not a word")
            continue

    # makes list of words

    tar_word_list = list(tar_word)

    guess_word_list = list(word)

# main logic

    '''
        itemizes guessed word into numbers
        0 = not in tar word
        1 = not in correct pos but is in word
        2 = in word & in correct pos
    '''
    i=0
    latest_guess = []
    while i < 5:
        if tar_word_list[i] == guess_word_list[i]:
            latest_guess.append(2)
        elif guess_word_list[i] in tar_word:
            latest_guess.append(1)
        else:
            latest_guess.append(0)
        i+=1

    '''
        if the letter is in the correct position and there is no duplicate in the target word of this letter.
        check the guess list for if it contains this letter twice if so AND one is in the correect position assigned 2 assign the other to 0 else assign both to 1
        e.g. 
            moist = 0,1,1,1,1
            stoat = 2,2,2,0,0
        word in senario == stoic
    '''
    # Adjust latest_guess for duplicate letters in the guessed word
    for x, letter in enumerate(guess_word_list):
        # If the guessed letter appears more than once
        if guess_word_list.count(letter) > 1:
            # Count occurrences of the letter in the target word
            target_letter_count = tar_word.count(letter)
            guess_letter_positions = [i for i, l in enumerate(guess_word_list) if l == letter]

            # Track how many correct and incorrect positions we've assigned
            correct_positions = 0
            incorrect_positions = 0

            # First, mark correct positions as `2`
            for pos in guess_letter_positions:
                if tar_word_list[pos] == letter:
                    latest_guess[pos] = 2
                    correct_positions += 1

            # Then, mark incorrect positions as `1` if the target word has extra instances
            for pos in guess_letter_positions:
                if latest_guess[pos] != 2:
                    if correct_positions + incorrect_positions < target_letter_count:
                        latest_guess[pos] = 1
                        incorrect_positions += 1
                    else:
                        latest_guess[pos] = 0  # Mark extra instances as `0` if target letter count is met


    # colours current word using itemised word and guessword list
    current_col_guess = []
    index_nums = 0
    for i in range(5):
        if latest_guess[i] == 2:
            current_col_guess.append((guess_word_list[i], 'green'))
        elif latest_guess[i] == 1:
            current_col_guess.append((guess_word_list[i], 'yellow'))
        else:
            current_col_guess.append((guess_word_list[i], 'red'))

    past_guesses.append(current_col_guess)

    #prints list of past words
    for guess in past_guesses:
        for letter, color in guess:
            cprint(letter, color, end=" ")
        print()

    # checks for correct word or maxed guesses
    if latest_guess == [2, 2, 2, 2, 2]:
        print("Well Done!")
        break
    elif guess_count == 6:
        print(f"Nice try, The word was {tar_word}")
        break
    else:
        continue

