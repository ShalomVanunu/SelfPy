
def check_valid_input(letter_guessed, old_letters_guessed):

    if (len(letter_guessed) ==1 and letter_guessed.lower()  not in  old_letters_guessed):
        if( letter_guessed.isalpha()): # is one of alphabet
             return True
        elif ( not letter_guessed.isalnum()): # is sign
             return False
    else:
            return False


def main(): # Call the function func
    old_letters = ['a', 'b', 'c']
    print(check_valid_input('s', old_letters))


if __name__ == "__main__":
    main()