import random

def hangman():
    word_list = ["python", "java", "javascript", "computer", "science"]
    word = random.choice(word_list)
    word = word.lower()
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    tries = 6
    while len(word_letters) > 0 and tries > 0:
        print("You have", tries, "tries left.")
        if len(used_letters) > 0:
            print("Used letters:", " ".join(used_letters))
        print(" ".join([letter if letter in used_letters else "_" for letter in word]))
        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                tries -= 1
        else:
            print("You have already used that letter. Try again.")
    if tries == 0:
        print("You lost! The word was", word)
    else:
        print("You won! The word was", word)

hangman()