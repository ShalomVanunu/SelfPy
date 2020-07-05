
temperature =input('Insert the temperature you would like to convert: ')
decitionCorF = temperature [-1:]
temperature_number = temperature [:-1]
#print(decitionCorF)
#print(temperature_number)
if (decitionCorF == 'C'):
   print(str((9*int(temperature_number)+(32*5))/5)+'F')
else:
    print(str((5*int(temperature_number)-160)/9)+'C')
