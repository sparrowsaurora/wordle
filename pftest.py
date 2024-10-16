import random as r
tw = open("target_words.txt", "r")
aw = open("all_words.txt", "r")
words = aw.read().split("\n")
guess_count = 0

#get random target word function
lines = tw.readlines()
tar_word = r.choice(lines)
print(tar_word)


while True:
    latest_guess = []
    #guessing mechanics
    while True:
        word = input("word >> ")
        if word in words:
            print("is word")
            guess_count += 1
            break
        else:
            print("not a word")
            continue
    # locate correct letter position or if letter in word
    """
    use tuples as a selector (0 = not in, 1 = in(not correct pos), 2 = in word & in correct pos)"""
    while i = 
    for letter in word:
        listed_word = listed_word.append(letter)
    for char in word:
        if char in tar_word and char in correct_position:
            latest_guess.append(2)
            continue
        elif char in tar_word:
            latest_guess.append(1)
            continue
        else:
            latest_guess.append(0)
            continue
    print(latest_guess)
    if guess == 6:
        print(tar_word)
        quit()
    else:
        continue