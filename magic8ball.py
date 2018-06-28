import random

question = input("What would you like to know? ")
 
# creates a temporary variable "x" to be defined

# range (1) says to generate only one number

# x = random.randint(1,20) generates a random number between 1 and 20 and defines it
# as that number

for x in range (1):
    #between 1 and 10
    x = random.randint(1,20)

# creates a list of different answers that will be called by their index number
# if their corresponding number is generated (the index will always be one value
# less than the number defined by "x")

answers = ["It is certain","It is decidedly so","Without a doubt","Yes - definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtfull"]


# if the number generated is 1, then print the string from "answers" with the index
# of 0 
if x == 1:
    print (answers[0])

elif x == 2:
    print (answers[1])

elif x == 3:
    print (answers[2])

elif x == 4:
    print (answers[3])

elif x == 5:
    print (answers[4])

elif x == 6:
    print (answers[5])

elif x == 7:
    print (answers[6])

elif x == 8:
    print (answers[7])

elif x == 9:
    print (answers[8])

elif x == 10:
    print (answers[9])

elif x == 11:
    print (answers[10])

elif x == 12:
    print (answers[11])

elif x == 13:
    print (answers[12])

elif x == 14:
    print (answers[13])

elif x == 15:
    print (answers[14])

elif x == 16:
    print (answers[15])

elif x == 17:
    print (answers[16])

elif x == 18:
    print (answers[17])

elif x == 19:
    print (answers[18])

elif x == 20:
    print (answers[19])

# if the number generated is not 1-20, print error

else:
    print ("Error")
   