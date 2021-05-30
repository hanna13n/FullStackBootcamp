import random

Repeat = 100
Correct = 200
Wrong = 300
Dead = 400
Success = 500


def get_word(fname):
    good_words = []
    f = open(fname)
    for i in f:
        i = i.strip()

        if len(i) < 5:
            continue
        if i.istitle():
            continue
        if not i.isalpha():
            continue

        good_words.append(i)
    return random.choice(good_words)


def mask_word(word, letters_to_show):
    op = []
    for i in word:
        if i in letters_to_show:
            op.append(i)
        else:
            op.append("_")
    return "".join(op)


def create_status(word, guesses, turns_left):
    guesses = " ".join(guesses)
    word = mask_word(word, guesses)
    return f"""Word :{word}
Guesses :{guesses}
Turns left :{turns_left}"""


def check_guess(word, letter, guesses, turns_left):
    all_guessed = True
    t = guesses+[letter]
    for i in word:
        if i not in t:
            all_guessed = False
    if all_guessed:
        return Success
    if letter in guesses:
        return Repeat
    elif letter in word:
        return Correct
    else:
        if turns_left == 1:
            return Dead
        else:
            return Wrong


def main():
    turns_left = 10
    guesses = []
    word = get_word("/usr/share/dict/words")
    while True:
        status = create_status(word, guesses, turns_left)
        print(status)
        guess = input("Enter input and hit enter ")

        r = check_guess(word, guess, guesses, turns_left)

        if r == Correct:
            guesses.append(guess)
        elif r == Repeat:
            print(f"You've already guessed '{guess}' ")
        elif r == Wrong:
            turns_left -= 1
            guesses.append(guess)
        elif r == Dead:
            print(f"Sorry! You've run out of turns. The word was '{word}'")
            break
        elif r == Success:
            print(f"Congratulation! You got it. the word was '{word}'")
            break


main()
