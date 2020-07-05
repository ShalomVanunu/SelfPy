

def sequence_del(my_str):
    new_string = []
    new_string.append(my_str[0])
    before_letter = my_str[0]
    for letter in my_str:
        while letter != before_letter:
            new_string.append(letter)
            before_letter = letter
    print(*new_string)



def main(): # Call the function func
    sequence_del("ppyyyyythhhhhooonnnnn")
   # 'python'
    sequence_del("SSSSsssshhhh")
   # 'Ssh'
    sequence_del("Heeyyy   yyouuuu!!!")
   # 'Hey you!'

if __name__ == "__main__":
    main()
