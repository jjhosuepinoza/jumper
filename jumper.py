import random
from words import word_list
import pygame



def get_word():
    word = random.choice(word_list)
    return word.upper()


def _play (word):
    _word_completion = "_" * len(word)
    _guessed = False
    _guessed_letters = [  ]
    _tries = 5
    print("π¬πͺ------------J U M P ER-----------πͺπ¬")
    print(_display_jumper(_tries))
    print(_word_completion)
    print("\n")
    while not _guessed and _tries > 0:
        guess = input("πͺGuess a letterπ¬ [A-Z] ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in _guessed_letters:
                print("π₯± You already wrote the letter",guess )
            elif guess not in word:
                print("π Nope")
                print("The letter ",guess," is not in the word.")
                _tries -= 1
                _guessed_letters.append(guess)
            else:
                print("π Well done!π,")
                print(guess, "is in the word!")
                _guessed_letters.append(guess)
                word_as_list = list(_word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                _word_completion = "".join(word_as_list)
                if "_" not in _word_completion:
                    _guessed = True
        else:
            print("πYou are not typing a letter.")
        print(_display_jumper(_tries))
        print(_word_completion)
        print("\n")
    if _guessed:
        print("πβ¨πYou won!πβ¨π")
    else:
        print("ππYou didn't get it.π» The word was " + word + ".")


def _display_jumper(tries):
    _stages = [  
              
               
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
    return _stages[tries]


def _main():
    _word = get_word()
    _play(_word)
    while input("π Play Again? (Y/N) ").upper() == "Y":
        _word = get_word()
        _play(_word)
    else:
        print("Goodbye!π₯" )
    


if __name__ == "__main__":
    _main()
pygame .quit()
