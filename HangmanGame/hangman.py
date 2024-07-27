from words import word_list
import random
def get_word():
    word = random.choice(word_list) #to get a randomly chosen word to use for the game from a list of 300 words
    return word.upper() #return that randomly chosen word in uppercase


def play(word): #creating a function called play containing all the instructions for the game
    word_completion = "_"* len(word) #will create a line of underscores with the length of the chosen word
    guessed = False #creates a variable called guess with the default value of false
    guessed_letters = [] #creates an array for the purpose of collecting the guessed letters for the current word
    guessed_words = [] #creates and array for the purpose of collecting the guessed words for the current word
    tries = 6 #creates a variable called tries so there is a limit of 6 guesses for the user to guess the word
    print("Let's play Hangman!") 
    print(display_hangman(tries)) 
    print(word_completion) #will print the line of underscores with the length of the chosen word
    print("\n") #goes on to the next line
    while not guessed and tries > 0: #while the current guessed is not in the guessed array and tries is greater than zero then ask the user to guess a letter or a word
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha(): #if the length of the guess is 1, and is in the alphabet that mean its a letter
            if guess in guessed_letters: #then if that letter guess is in the guessed letters array, then print the message below
               print("You already guessed the letter")
            elif guess not in word: #otherwise print the message that says thre user's guess is not in the word
                 print(guess, "is not in the word.") 
                 tries -= 1 #decrement the number of guesses by 1 everytime the user guesses a different letter that is not in the word 
                 guessed_letters.append(guess) #then add that guess to guessed letters array
            else: #if the guess is part of the word, then print the message below
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
               print("You already guessed the word", guess)
            elif guess != word:
                 print(guess, "is not the word.")
                 tries -= 1
                 guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
       print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()