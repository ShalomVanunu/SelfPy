

def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    if (len(letter_guessed) ==1 and letter_guessed.lower()  not in  old_letters_guessed):
        if( letter_guessed.isalpha()): # is one of alphabet
             old_letters_guessed.append(letter_guessed.lower())
             print(old_letters_guessed)
             return True
        elif ( not letter_guessed.isalnum()): # is sign
             print('X')
             print ( "->".join(sorted(old_letters_guessed)))
             return False
    else:
        print("->".join(sorted(old_letters_guessed)))
        print('X')
        return False


def main(): # Call the function func
    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed('A', old_letters))

    print(try_update_letter_guessed('s', old_letters))

    print(old_letters)

    print(try_update_letter_guessed('$', old_letters))

    print(try_update_letter_guessed('d', old_letters))

    print(old_letters)


if __name__ == "__main__":
    main()