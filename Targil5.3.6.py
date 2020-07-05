

def filter_teens(a=13, b=13, c=13):
    """check if number is value 13"""
    sum = abs(13-a)+abs(13-b)+abs(13-c) #check the diff
    if (sum == 0):
        print(sum)
    else:
       if (a == 13 ):
         print (b+c)
       elif (b == 13):
         print(a+c)
       elif (c == 13):
         print(b+a)
       else:
        print(a+b+c)




filter_teens()
filter_teens(1, 2, 3)
filter_teens(2, 13, 1)
filter_teens(2, 1, 15)