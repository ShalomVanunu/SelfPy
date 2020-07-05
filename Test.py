dict_list = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970",
             "hobbies": ['Sing', 'Compose', 'Act']}

date_tuple = ()
day_tuple = dict_list['birth_date'][0:2]
month_tuple = dict_list['birth_date'][3:5]
year_tuple = dict_list['birth_date'][6:10]
date_tuple = (day_tuple,month_tuple,year_tuple)

print((date_tuple))

print('my name is {0} and my last name {1}'.format('shalom',4))

print(17%10)
tuple_list = (1, 3,7)
print(tuple_list)
(value1, value2 , value3)= (1 , 4, 6)
print(value1)

old_letters = ['a', 'b', 'd']
check_valid_input= 'C'
if (check_valid_input.lower() in old_letters):
     print(True)
else:
    print(False)

x =  [5,6,7,8,9]
for i in x:
    print(i)


first_list = [0,1,2]
second_list = [3, 4, 5]
sum_list = first_list+second_list
print(sum_list)