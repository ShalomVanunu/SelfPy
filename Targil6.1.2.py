

def shift_left(my_list):
    a , b ,c = my_list
    new_my_list = [b ,c, a]
    print(new_my_list)


def main(): # Call the function func
    shift_left([0, 1, 2])
    shift_left(['monkey', 2.0, 1])

if __name__ == "__main__":
    main()
