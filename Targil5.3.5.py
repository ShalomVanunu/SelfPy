
def distance(num1, num2, num3):
    num1_num2 = abs(num2-num1)
    num3_num2 = abs(num3-num2)
#    print(num3_num2)
#    print(num1_num2)
    if (num1_num2 == 1 and num3_num2 > 2 ):
        return True
    else:
        return False

print('distance(1, 2, 10)')
print(distance(1, 2, 10))
print('distance(4, 5, 3)')
print(distance(4, 5, 3))

