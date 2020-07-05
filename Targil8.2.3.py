

def mult_tuple(tuple1, tuple2):
    lenth_of_tuple1 = len(tuple1)
    lenth_of_tuple2 = len(tuple2)
    new_list_tuple = ()
    temp_tuple = ()
    for times1 in range(lenth_of_tuple1):
        for times2 in range(lenth_of_tuple2):
            temp_tuple = tuple1[times1],tuple2[times2]
            new_list_tuple += temp_tuple,
            temp_tuple = tuple2[times2], tuple1[times1]
            new_list_tuple += temp_tuple,
    print(new_list_tuple)

def main(): # Call the function func
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    mult_tuple(first_tuple, second_tuple)
  #  ((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))

    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    mult_tuple(first_tuple, second_tuple)
 #((1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 1), (5, 1), (6, 1), (4, 2), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3))

if __name__ == "__main__":
    main()
