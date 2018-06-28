#lists can hold any number of strings. They can even hold other lists
another_list = ["yeet","yote"]
#when using a list in a list, the list you are using inside of another counts 
#as one element in the list (you get what i mean)
my_list =["apple","pear","orange","1",another_list]

#this prints the numerical value of elements in a list
print(len(my_list))

#this adds "banana" to my_list
my_list.append("banana")

print (my_list)

#tells the program to remove the latest string from the list (pretending)
#like its a stack of papers (removing the last string in the list)
my_list.pop()

#the number in the parentheses of .pop() will remove the corresponding 
#string from the list. 0 being the first string and so on
my_list.pop(0)

print (my_list)
#since i defined this variable after I had removed apple and bannana from
#the list, it left pear as the string 0
my_fruit = my_list.pop(0)

print(my_fruit)

#replaces the inexed string with "banana", the index being 1
my_list.insert(1,"banana")

print (my_list)
#removes "banana" from the list
my_list.remove("banana")

print (my_list)
#adds "mango" and "watermalon" to my_list
my_list.extend (["mango","watermelon"])

print (my_list)


#takes the strings indexed 0-2 (2 strings) and uses them in new_list
#this takes string 0-1, and the 2 tells it to stop there

new_list = my_list[0:2] 

print (new_list)

yeet_list = my_list[0]

print (yeet_list)

)
yote_list = my_list[2]

print (yote_list