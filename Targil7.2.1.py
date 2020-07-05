

def is_greater(my_list, n):
   big_numbers = []
   for number in my_list:
       if number > n:
           big_numbers.append(number)
   return  big_numbers



def main(): # Call the function func
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)
   # [30, 60]

if __name__ == "__main__":
    main()
