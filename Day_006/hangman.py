import random as rrr


hangman_words = [
    "apple", "house", "beach", "cloud", "smile", "train", "water", "music", "light", "chair",
    "elephant", "giraffe", "kangaroo", "dolphin", "penguin", "crocodile", "butterfly", "octopus", "squirrel", "chimpanzee",
    "strawberry", "broccoli", "spaghetti", "pancake", "pineapple", "avocado", "chocolate", "zucchini", "blueberry", "sandwich",
    "refrigerator", "microwave", "television", "computer", "pillow", "blanket", "window", "cabinet", "mirror", "curtain",
    "galaxy", "algorithm", "internet", "telescope", "molecule", "gravity", "chemistry", "software", "hardware", "database",
    "mountain", "volcano", "waterfall", "continent", "hurricane", "glacier", "canyon", "peninsula", "archipelago", "monsoon",
    "knowledge", "adventure", "mystery", "surprise", "imagination", "philosophy", "curiosity", "opportunity", "perseverance", "independence",
    "whisper", "calculate", "explore", "discover", "celebrate", "communicate", "juggle", "negotiate", "fascinate", "recommend",
    "rhythm", "jazz", "puzzle", "wizard", "queue", "awkward", "xylophone", "zigzag", "jukebox", "oxygen",
    "umbrella", "guitar", "pirate", "castle", "dragon", "shadow", "diamond", "symphony", "bicycle", "library"
]


stages = [
  """
     +---+
     |   |
         |
         |
         |
         |
  =========
  """,
  """
     +---+
     |   |
     O   |
         |
         |
         |
  =========
  """,
  """
     +---+
     |   |
     O   |
     |   |
         |
         |
  =========
  """,
  """
     +---+
     |   |
     O   |
    /|   |
         |
         |
  =========
  """,
  """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
  =========
  """,
  """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
  =========
  """,
  """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
  =========
  """
]


word = rrr.choice(hangman_words)
word_list = list(word)
letlist = ["_"] * len(word)
guessed_letters = []
man = 0
ON = True

print("Welcome to Hangman!!! Guess a letter to start rolling 🎯")
print(stages[man])
print(" ".join(letlist))


while ON:
    guess = input("\nEnter a letter: ").lower()

    # Checking for duplicate guess
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'! Try something new 😅")
        continue
    else:
        guessed_letters.append(guess)

    match_found = False

    for i, item in enumerate(word_list):
        if guess == item:
            letlist[i] = guess
            match_found = True

    if match_found:
        print(f"{guess} is a correct guess... You’re a mind reader, machine killer 😎")
    else:
        man += 1
        print(f"OOPS! '{guess}' is not in the word 😢")

    print(stages[man])
    print(" ".join(letlist))
    print(f"Guessed letters so far: {', '.join(guessed_letters)}")


    if "_" not in letlist:
        print("\n🏆 YOU WON, LEGEND! The word was:", word)
        ON = False


    elif man >= 6:
        print("\n💀 GAME OVER... Thanks for playing, pookie :)")
        print(f"The word was: {word}")
        ON = False
