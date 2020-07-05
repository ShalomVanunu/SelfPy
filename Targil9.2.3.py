
def who_is_missing(file_name):
    number =0
    source_file = open(file_name,'r').read()
    sorted_numbers = sorted(source_file.split(','))
    for index_num in sorted_numbers:
        if (int(index_num)-number) != 1:
            number =int(index_num)-1

            print(number)
            break
        else:
            number = int(index_num)

    destination_file = open(r"C:\Users\Shalom\PycharmProjects\Selfpy\found.txt",'w')
    destination_file.write(str(number))



def main():  # Call the function func
    who_is_missing(r"C:\Users\Shalom\PycharmProjects\Selfpy\findMe.txt")


if __name__ == "__main__":
    main()