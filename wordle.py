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
tar_word = r.choice(lines)


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

    tar_word_list = list(tar_word)

    guess_word_list = list(word)

#itemizes guessed word into numbers
# 0 = not in tar word
# 1 = not in correct pos but is in word
# 2 = in word & in correct pos
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

