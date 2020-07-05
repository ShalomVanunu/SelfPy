
sentence = input("Please enter a string: ")
lenth_sentence = len(sentence)
half_lenth_sentence = lenth_sentence//2
pharse1 = sentence[:half_lenth_sentence]
pharse2 = sentence[half_lenth_sentence:]
print(pharse1+pharse2.upper())
#print(sentence.upper())
