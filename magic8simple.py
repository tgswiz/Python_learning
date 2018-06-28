import random

question = input("What would you like to know? ")

for x in range (1):
    #between 1 and 10
    x = random.randint(1,20)

answers = ["Yes","No","Maybe so"]

while x < 11:
    print (answers[0])

    break

while x >10 & x <21:
    print (answers[1])

    break






