
def show_hidden_word(secret_word, old_letters_guessed):
    hidden_word = []
    for letter in secret_word:
        if letter not in old_letters_guessed:
            hidden_word.append(' _')
        else:
            hidden_word.append(letter)

    return ' '.join(hidden_word)

def main(): # Call the function func
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))
  #  m _ m m _ _s
    secret_word = "mammals"
    old_letters_guessed = [ ]
    print(show_hidden_word(secret_word, old_letters_guessed))

if __name__ == "__main__":
    main()