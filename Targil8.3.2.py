import datetime
current_year = datetime.date.today().year

def dict_task(dict_list):
    date_tuple = ()
    number_choosen = 0
    while number_choosen < 7:
        number_choosen = int(input('Please enter number :'))
        if number_choosen == 1:
            print(dict_list['last_name'])
        elif number_choosen == 2:
            print(dict_list['birth_date'][3:5])
        elif number_choosen == 3:
            print(len(dict_list['hobbies']))
        elif number_choosen == 4:
            print(dict_list['hobbies'][-1])
        elif number_choosen == 5:
            print('Adding Cooking to hobbies')
            dict_list['hobbies'].append('Cooking')
            print(dict_list['hobbies'])
        elif number_choosen == 6:
            date_tuple = ()
            day_tuple = dict_list['birth_date'][0:2]
            month_tuple = dict_list['birth_date'][3:5]
            year_tuple = dict_list['birth_date'][6:10]
            date_tuple = (day_tuple, month_tuple, year_tuple)
            print(date_tuple)
        elif number_choosen == 7:
            birth_year = dict_list['birth_date'][6:10]
            print(int(current_year)-int(birth_year))






def main(): # Call the function func
    dict_list = {"first_name":"Mariah","last_name":"Carey","birth_date":"27.03.1970","hobbies":['Sing', 'Compose', 'Act']}
    dict_task(dict_list)

if __name__ == "__main__":
    main()
