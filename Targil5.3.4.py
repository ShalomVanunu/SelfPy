
def last_early(my_str):

    last_word = my_str[-1]
    new_my_str = my_str[:-1]
    if (last_word in new_my_str):
        return True
    else:
        return False


sentence = input('write a sentence :')
print(last_early(sentence))