def take_second(elem):
    return elem[1]

def sort_prices(list_of_tuples):
    new_list_tuple = sorted(list_of_tuples, key = take_second, reverse=True)
    print(new_list_tuple)

def main(): # Call the function func
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    sort_prices(products)
   # [('bread', '9.0'), ('milk', '5.5'), ('candy', '2.5')]

if __name__ == "__main__":
    main()
