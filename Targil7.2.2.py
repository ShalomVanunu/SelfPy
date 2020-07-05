
def numbers_letters_count(my_str):
    count_numbers = 0
    count_letters = 0
    result = [0,0]
    for letter in my_str :
        if letter.isdigit():
            count_numbers +=1
        else:
            count_letters +=1
    result[0] = count_numbers
    result[1] = count_letters
    return result

def main(): # Call the function func
    print(numbers_letters_count("Python 3.6.3"))
    #[3, 9]

if __name__ == "__main__":
    main()
