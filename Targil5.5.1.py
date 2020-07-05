

def is_valid_input(letter_guessed):
    if (len(letter_guessed) ==1 ):
        if( letter_guessed.isalpha()):
           #  print (letter_guessed.lower())
             return True
        elif ( not letter_guessed.isalnum()):
           #  print('E2')
             return False
    else:
        if (letter_guessed.isalpha()):
         #   print('E1')
            return False
        else:
           # print('E3')
            return False

def main(): # Call the function func
    letter_guessed = input('Guess a letter: ')
    print(is_valid_input(letter_guessed))

if __name__ == "__main__":
    main()
