
def seven_boom(end_number):
    boom7 = []
    number = 0
    while number < end_number+1:
        if number % 7 == 0 :
            boom7.append('BOOM')
            number += 1
        elif number % 10 == 7:
            boom7.append('BOOM')
            number += 1
        else:
            boom7.append(number)
            number += 1
    return boom7


def main(): # Call the function func
    print(seven_boom(17))
    #['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM']

if __name__ == "__main__":
    main()
