


def task_list(my_str):
    list_names =  list(my_str.split(","))
    number_choosen = 0
    while number_choosen < 10:
        number_choosen = int(input('Please enter number :'))
        if number_choosen == 1:
            print(list_names)
        elif number_choosen == 2:
            print(len(list_names))
        elif number_choosen == 3:
            name_of_pruduct = input('Lets check if the product exsist :')
            if name_of_pruduct in list_names:
                print(True)
            else:
                print(False)
        elif number_choosen == 4:
            name_of_pruduct = input('Lets check how many the product exsist :')
            print(list_names.count(name_of_pruduct))
        elif number_choosen == 5:
            name_of_pruduct = input('Lets delete the product :')
            list_names.remove(name_of_pruduct)
            print(list_names)
        elif number_choosen == 6:
            name_of_pruduct = input('Lets add a product :')
            list_names.append(name_of_pruduct)
            print(list_names)
        elif number_choosen == 9:
            break





def main(): # Call the function func
    task_list("Milk,Cottage,Tomatoes")


if __name__ == "__main__":
    main()
