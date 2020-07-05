
COMMA = ', '
dates =''
#path_file = 'C:\Users\Shalom\PycharmProjects\SelfPy\Test.txt'
file_selected = open(r'C:\Users\Shalom\PycharmProjects\Campus\Test.txt', 'r')
for row in file_selected:
    dates += row.split(COMMA)[1]
file_selected.close()
print(dates)

saved_file = open(r'C:\Users\Shalom\PycharmProjects\Campus\saved1.txt','w')
saved_file.write(dates)