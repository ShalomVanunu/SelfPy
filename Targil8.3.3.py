
def count_chars(my_str):
    list_dict = {}
    for leter_count in my_str:
        if leter_count != ' ':
            list_dict[str(leter_count)] = my_str.count(leter_count)
    print(list_dict)

def main():  # Call the function func
    magic_str = "abra cadabra"
    count_chars(magic_str)
    # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}


if __name__ == "__main__":
    main()
