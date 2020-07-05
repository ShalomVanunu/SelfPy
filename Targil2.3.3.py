
number_blocks = input('Enter three digits (each digit for one pig):')
pig1 =  (int(number_blocks)//100)
pig2 = (int(number_blocks)//10%10)
pig3=  (int(number_blocks)%10)
print(pig1+pig2+pig3)
print((pig1+pig2+pig3)//3)
print((pig1+pig2+pig3)%3)
print(bool((pig1+pig2+pig3)%3) == 0)