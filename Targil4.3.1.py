
letter = input('Guess a letter: ')

if (len(letter) ==1 ):
    if( letter.isalpha()):
         print (letter.lower())
    elif ( not letter.isalnum()):
         print('E2')
else:
    if (letter.isalpha()):
        print('E1')
    else:
        print('E3')

