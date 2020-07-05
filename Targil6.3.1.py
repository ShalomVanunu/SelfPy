



def are_lists_equal(list1, list2):
    list1_order = sorted(list1)
    list2_order = sorted(list2)
    if (list1_order == list2_order):
         return  True
    else:
        return False


def main(): # Call the function func
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    print(are_lists_equal(list1, list2))
    print(are_lists_equal(list1, list3))

if __name__ == "__main__":
    main()
