

def format_list(my_list):
    size_of_list = len(my_list)
    my_new_list = my_list[0:size_of_list:2]
    last_word = my_list[-1:]
    print(my_new_list)

    print (', '.join(my_new_list), ', and', ', '.join(last_word))


def main(): # Call the function func
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    format_list(my_list)

    my_list = ["1", "2", "3", "4"]
    format_list(my_list)

if __name__ == "__main__":
    main()
