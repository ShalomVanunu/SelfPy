

# declaration of variables
###########################
secret_word = '' # The word that the player must guess
old_letters_guessed =[] # The letters the player guessed
MAX_TRIES =6 # maximum tries the player can guess
num_of_tries = 1 # The number the played guessed and didnt success
more_than_letter = False

def show_header():
    """
    this function print on the screen
    the Program Header Hangman
    """
    print("""     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \\
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |
                        |___/ 
    """)


def define_hangman_photos():
    """
    this function holds the pictures
    of the hangman stages in dictionary
    """
    HANGMAN_PHOTO = {} # The dictionary of pictures hangman

    # Picture1
    TGREEN =  '\033[32m' # Green Text
    ENDC = '\033[m'  # reset to the defaults
    HANGMAN_PHOTO[1] = (TGREEN + """    x-------x  """+ENDC)

    # Picture2
    HANGMAN_PHOTO[2] = (TGREEN +"""    x-------x"""+ENDC+"""
    |
    |
    |
    |
    |""")

    # Picture3
    HANGMAN_PHOTO[3] = (TGREEN +"""    x-------x"""+ENDC+"""
    |       |
    |       0
    |
    |
    |""")

    # Picture4
    HANGMAN_PHOTO[4] = (TGREEN +"""    x-------x"""+ENDC+""" 
    |       |
    |       0
    |       |
    |
    |""")

    # Picture5
    HANGMAN_PHOTO[5] = (TGREEN +"""    x-------x"""+ENDC+"""
    |       |
    |       0
    |      /|\\
    |
    |
    """)

    # Picture6
    HANGMAN_PHOTO[6] = (TGREEN +"""    x-------x"""+ENDC+"""
    |       |
    |       0
    |      /|\\
    |      /
    |""")

    # Picture7
    HANGMAN_PHOTO[7] = (TGREEN +"""    x-------x"""+ENDC+"""
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")
    return HANGMAN_PHOTO

def print_hangman(dict, num_of_tries):
    """
    this function print the right picture
    of the hangman

    dict holds the dictionary of the pictures
    num_of_tries holds the picture of the try
    """
    print(dict[num_of_tries]) # num_of_tries is the argument holds times

def choose_word(file_path, index):
    """
    this function returns the word that choose the player
    on the input

    index holds the word index on the file list
    file_path holds the path of the file containing the words
    """
    input_file = open(file_path , 'r').read() # loading the content of file
    list_of_word = input_file.split(' ') # split with spaces
    count_of_words = len(list_of_word) # counts how many words are in the file for Cycle
    secret_word = list_of_word[((index-1)%count_of_words)]  # making Cycle after the last word
    return secret_word # return the word

def check_valid_input(letter_guessed, old_letters_guessed):
    """
       this function check if the letter that entered is good

       letter_guessed holds the letter that entered by the user
       old_letters_guessed holds the old letters the user guessed earlier
       """
    if (len(letter_guessed) ==1 and letter_guessed.lower()  not in  old_letters_guessed):
        if( letter_guessed.isalpha()): # is one of alphabet
             return True
        elif ( not letter_guessed.isalnum()): # is sign
             return False
    else:
            return False

def show_hidden_word(secret_word, old_letters_guessed):
    """
    this function show the hidden words by
    the old letters that the player guessed

    secret_word holds secret word
    old_letters_guessed holds letters that the player already guessed
    """

    hidden_word = []
    for letter in secret_word:
        if letter not in old_letters_guessed:
            hidden_word.append(' _')
        else:
            hidden_word.append(letter)

    return ' '.join(hidden_word)

def try_update_letter_guessed(secret_word,letter_guessed, old_letters_guessed):
    """
        this function show the letter that was guessed
        by the user earlier

        secret_word holds secret word
        letter_guessed  holds the letter guessed by the user
        old_letters_guessed holds letters that the player already guessed
        more_than_letter
        """

    global num_of_tries  , more_than_letter # enable to use the argument
    if ((letter_guessed.lower()  in  old_letters_guessed) or (more_than_letter == True)): # check if the letter was guessed
        print('X')
        print("->".join(sorted(old_letters_guessed)))
        more_than_letter = False
        return False
    elif (letter_guessed.lower() not in secret_word): #check if the letter  inst on the word
        old_letters_guessed.append(letter_guessed.lower()) # add the letter for later
        print(':(')
        print_hangman(define_hangman_photos(), num_of_tries)
        num_of_tries+=1 # add 1 to count because there is a limit guessed
        return num_of_tries

    else:
        old_letters_guessed.append(letter_guessed.lower())
        return True

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    this function check if the letter that the player guessed
    is Valid and dont guessed earlier

    letter_guessed holds the letter player guessed
    old_letters_guessed holds letters that the player already guessed
    """
    global  more_than_letter
    more_than_letter = False
    if (len(letter_guessed) == 1 ):
        if(letter_guessed.isalpha()): # is one of alphabet
             return True
        elif (not letter_guessed.isalnum()): # is sign
             return False
    elif (len(letter_guessed) > 1 ):
         more_than_letter = True # sign for two letters
         return True
    else:
         return False

def check_win(secret_word, old_letters_guessed):
    """
       this function check if the word

       secret_word holds the secret word
       old_letters_guessed holds letters that the player already guessed
    """
    hidden_word = []
    for letter in secret_word:
        if letter not in old_letters_guessed:
            hidden_word.append('_')
        else:
            hidden_word.append(letter)
    new_word = ''.join(hidden_word)
    if secret_word == new_word: # check if the secret word contains all th e letters guessed
        return False
    else:
        return True

def reading_word_from_file():
    """
       this function show the information the user need to enter
     """
    global secret_word
    file_path = input('Enter file path: ')  # Get the Path of the file
    index_word = input('Enter index: ')  # Get the place of the word in file
    print('\n Let’s start! \n')
    secret_word = choose_word(file_path, int(index_word))


def main():  # Call the functions
    global num_of_tries , more_than_letter # declare of global
    show_header() #show the heaser text
    reading_word_from_file() # reading the file word content
    print_hangman(define_hangman_photos() , num_of_tries) # print the start hangman picture
    num_of_tries += 1 # readiness fot he next picture
    while (check_win(secret_word , old_letters_guessed) and (num_of_tries < MAX_TRIES+2)): # check if you start guess all letters and exceed tries
        letter_guessed = input("Guess a letter :") # read for letter
        if check_valid_input(letter_guessed, old_letters_guessed): # check the validation of letter
            if (try_update_letter_guessed(secret_word , letter_guessed , old_letters_guessed)): # check the letter entered
                 print(show_hidden_word(secret_word , old_letters_guessed)) # print the hidden word
        else:
            print('X') # wrong valid letter
    if num_of_tries == MAX_TRIES+2: # check the time you entered the mount of letters
        print('LOSE')
    else:
        print('WIN')


if __name__ == "__main__": # Run the main program
    main()