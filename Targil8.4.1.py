
def define_hangman_photos():
    HANGMAN_PHOTO = {}

    # Picture1
    HANGMAN_PHOTO[1] = ("""    x-------x 
    """)

    # Picture2
    HANGMAN_PHOTO[2] = ("""    x-------x
    |
    |
    |
    |
    |""")

    #Picture3
    HANGMAN_PHOTO[3] = ("""    x-------x 
    |       |
    |       0
    |
    |
    |""")

    #Picture4
    HANGMAN_PHOTO[4] = ("""    x-------x 
    |       |
    |       0
    |       |
    |
    |""")

    #Picture5
    HANGMAN_PHOTO[5] = ("""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""")

    #Picture6
    HANGMAN_PHOTO[6] = ("""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""")

    #Picture7
    HANGMAN_PHOTO[7] = ("""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")
    return HANGMAN_PHOTO

def print_hangman(dict, num_of_tries):
    print(dict[num_of_tries])


def main():  # Call the function func
    dict = define_hangman_photos()
    num_of_tries = 7
    print_hangman(dict , num_of_tries)

if __name__ == "__main__":
    main()

