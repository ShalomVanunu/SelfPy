

def extend_list_x(list_x, list_y):
   # new_list_x = str(list_x).strip('[]')
   # new_list_x = ', ' .join(map(str, list_x))
   # list_y.append(new_list_x)
   #print(list_y)
    joined_list = [*list_y, *list_x] # unpack both iterables in a list literal
    print(joined_list)




def main(): # Call the function func
  x = [4, 5, 6]
  y = [1, 2, 3]
  extend_list_x(x, y)

if __name__ == "__main__":
    main()
