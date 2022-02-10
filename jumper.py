import random
from words import word_list
import pygame



def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 5
    print("🛬🪂------------J U M P ER-----------🪂🛬")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("🪂Guess a letter🛬 [A-Z] ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("🥱 You already wrote the letter",guess )
            elif guess not in word:
                print("😜 Nope")
                print("The letter ",guess," is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("😎 Well done!😎,")
                print(guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("👀You are not typing a letter.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("🌄✨🎉You won!🎉✨🌄")
    else:
        print("🙀😅You didn't get it.👻 The word was " + word + ".")


def display_hangman(tries):
    stages = [  
              
               
                """
                   
                   x
                  \ /
                   |      
                  / \\
                """,
          
                """
               
                  \ /
                   O
                  \ /
                   |      
                  / \\
                """,
             
                """
                   
                 \   /
                  \ /
                   O
                  \ /
                   |     
                  / \\
                """,
              
                """
                  ___
                 \   /
                  \ /
                   O
                  \ /
                   |     
                  / \\
                """,
         
                """
                 /___\\
                 \   /
                  \ /
                   O
                  \ /
                   |
                  / \\
                """,
              
                """ 
                  ___ 
                 /___\\
                 \   /
                  \ /
                   O
                  \ /
                   |
                  / \\

                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("😏 Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
    else:
        print("Goodbye!😥" )

if __name__ == "__main__":
    main()
pygame .quit()