


def choose_word(file_path, index):

    new_list = []
    count_list = 0
    result_word = ()
    input_file = open(file_path,'r').read() #loading the content of file

    list_of_word = input_file.split(' ') # split with enter
  #  print(list_of_word)
  #  print(list_of_word[(index-1)%14])

    for word_in_list in list_of_word:
        if word_in_list not in new_list:
            new_list.append(word_in_list)
            count_list += 1
   # print(count_list)
    result_word = (count_list,list_of_word[(index-1)%14])
    print(result_word)

def main():  # Call the function func

    choose_word(r"C:\Users\Shalom\PycharmProjects\Selfpy\words.txt", 3)
    #(9, 'most')
    choose_word(r"C:\Users\Shalom\PycharmProjects\Selfpy\words.txt", 15)

if __name__ == "__main__":
    main()