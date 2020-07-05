sentence = input('Enter a word: ')
reverse_sentence = sentence [::-1]

if (reverse_sentence.upper().replace(" ","") == sentence.upper().replace(" ","")):
    print('OK')
else:
    print('NOT')
