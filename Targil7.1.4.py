





def squared_numbers(start, stop):
    i= start
    list_squared_numbers = []
    while  i < stop+1:
            list_squared_numbers.append(i**2)
            i +=1
    print(list_squared_numbers)



def main(): # Call the function func
    squared_numbers(4, 8)
   # [16, 25, 36, 49, 64]
    squared_numbers(-3, 3)
   # [9, 4, 1, 0, 1, 4, 9]

if __name__ == "__main__":
    main()
