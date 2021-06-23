import random
import sys

#  |    |
#  |    0
#  |   /#\
#  |   / \



#Dictionary that contains an array of words
items= {
    'color' : [        'blue',         'yellow',        'green',        'black',        'white'    ],
    'country' : [
        'argentina', 
        'bolivia', 
        'brasil', 
        'chile', 
        'colombia', 
        'ecuador', 
        'paraguay', 
        'peru', 
        'uruguay', 
        'venezuela'
    ],
    'animal' : [
        'mono',
        'jirafa',
        'gato',
        'perro',
        'jabali',
        'elefante',
        'pez',
        'cocodrilo',
        'rinoceronte',
        'caballo'
    ]
}

# Welcome message
def welcome():
    print(
        """
        Welcome to the game, the rules are pretty easy, you wil promted with the type of word
        an then, you will have to start guessing the letters!

        Lets start...


        """
    )

# Function that randomly gets the type and word to play from the "items" dictionary
def getTheWord():
    # aux = list(items.keys())
    # type_of_word = random.choice(aux)

    type_of_word = random.choice(list(items.keys()))    # ["color", "animal", "pais"]
    word = random.choice(items[type_of_word])           # items["animal"]

    return type_of_word, word

# Function that draw the stick figure
def draw_figure(array_de_guines_bajos, errors):
    stick_man = [
        " |",                                               #0 - Sin Errores
        " |    0",                                          #1 - 1 error
        " |    0\n |   /",                                  #2 - 2 errores
        " |    0\n |   /#",                                 #3
        " |    0\n |   /#\\ ",                              #4
        " |    0\n |   /#\\ \n |   /",                      #5
        " |    0\n |   /#\\ \n |   / \\ ",                  #6
    ]
    print(" |--------")
    print(" |    |")
    print(stick_man[errors])
    print("_|__________")
    for un_caracter in array_de_guines_bajos:
        print(un_caracter, end = ' ')                         # https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
    return 0

# Main game
def hangman():
    is_playing = True
    arrayAux = []
    type_of_word, word = getTheWord()
    errors = 0

    for letra in word:
        arrayAux.append('_')

    print(
        """
        The type of the word is '""" + type_of_word + """'!!!
        The word have """ + str(len(word)) + """ characters!!!
        Good Luck!!
        """
    )

    while is_playing:
        if '_' not in arrayAux:
            print(
                """
                Congratulations!!!
                YOU WIN!!!
                """
            )
            is_playing = False
            break

        draw_figure(arrayAux, errors)
        
        print()
        letter = str.lower(input("Choose a letter or '0' (Zero) to exit: "))

        if letter == '0':
            sys.exit()

        if letter in word:
            print('Letter found!')

            for position in range(len(arrayAux)):
                if letter == word[position]:
                    arrayAux[position] = letter
        else:
            print('Wrong letter!')
            errors = errors + 1
            if errors == 6:
                draw_figure(arrayAux, errors)
                print(
                    """
                    Noooooooo!!!
                    YOU LOSE!!!
                    The word was: {0}
                    """. format(word))
                sys.exit()


if __name__ == '__main__':
    welcome()
    hangman()