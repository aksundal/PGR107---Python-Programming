import random

def run(words,words_guessed):

    while len(words_guessed) < len(words):
        # Chooses word from array that are not guessed.
        word = random.choice([w for w in words if w not in words_guessed])
        # Make a hidden form of word.
        secret_word = '_' * len(word)
        #Stores data about guesses, number of wrong guesses and how many turns is still available.
        guesses = []
        wrong = 0
        turns = len(word)
        #Starting game.
        print("Your words to guess: ", (len(words) - len(words_guessed)))
        print("Let's play, Ninja! Here comes the word:")
        print("_" * 30)
        # The while loop that runs when there are still attempts to guess the letter or the words is not already guessed.
        while wrong < turns and secret_word != word:
            print("You have ", turns - wrong, " wrong guesses left")
            print("Your word looks like this: ", secret_word)
            #Input from user.
            guess = input("Enter a letter: ").lower().strip()
            #Check that input is valid.
            if not guess or len(guess) > 1 or not guess.isalpha():
                print("Focus,Ninja! Enter valid input!")
                continue
            if guess in guesses:
                print("Something blinded you? You already guessed this letter!")
                continue

            guesses.append(guess)
            #Find out if letter is in word.
            if guess in word:
                print("Good job, Ninja! Kakashi Sensei will be proud! That letter is in the word.")
                secret_word = ''.join([guess if word[i] == guess else secret_word[i] for i in range(len(word))])
            else:
                print("Concentrate!You'll do better next time!")
                wrong += 1
        print("_" * 30)
        #Check if the user guessed the word or not.
        if secret_word == word:
            print("Your are good, Ninja! You guessed the word: ", word)
            words_guessed.append(word)
        else:
            print("Ninja! You can do it!")
        print("_" * 30)
        play_again = input("Do you want to play again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("Thanks for the game! Come back when you are ready to guess all the words!")
            break
    return words_guessed
#Just function to generate prize
def generate_prize():
    prizes = ["ramen", "shuriken","kunai","Kakashi's Sensei book"]
    prize = random.choice(prizes)
    return prize

def main():
    #Open file and check that there are no issues.
    try:
        file = open("words.txt", "r")
        words = file.read().splitlines()
        if not words:
            raise ValueError("File is empty.")
    except FileNotFoundError:
        print("File does not exist.")
        return
    except ValueError as e:
        print(e)
        return
    file.close()
    # Variable for storage of guessed words.
    words_guessed = []
    name = input("Hello, Ninja. Enter your name-->")
    print(f"Welcome to my Naruto Word Guessing Game,{name}. Your mission for today is to guess all the words to prove that you are real shinobi.", name)

    #Return array of guessed words.
    result = run(words, words_guessed)
    # When length of guessed words is same as original array of words - user won the game.
    if len(result) == len(words):
       print("Wow! You guessed all the words! You are REAL shinobi. Congratulations and take your prize: ")
       print("Here is your prize--->",generate_prize())
    else:
        print(f"Words guessed: {len(result)} out of {len(words)}.")

if __name__ == "__main__":
    main()

