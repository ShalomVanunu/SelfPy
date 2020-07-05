

def check_win(secret_word, old_letters_guessed):
    hidden_word = []
    for letter in secret_word:
        if letter not in old_letters_guessed:
            hidden_word.append('_')
        else:
            hidden_word.append(letter)
    new_word = ''.join(hidden_word)
    #print(new_word)
    if secret_word == new_word:
        return True
    else:
        return False

def main(): # Call the function func
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))
   # False
    secret_word = "friends"
    old_letters_guessed = ['f', 'i', 'r', 'e', 'n', 'd', 's']
    print(check_win(secret_word, old_letters_guessed))
   # False

if __name__ == "__main__":
    main()