#specifies contents of the .txt file and defines it as a variable
text_contents = "henlo bepis its conk. how r u doin bro?"

#says to open a file named hey.txt, and if it doesnt exist, create it
text_hey = open("hey.txt", "w+")

#says to write the contents of text_contents to the text_hey variable, 
#which in turn, writes it to the hey.txt file
text_hey.write(text_contents)

#this tells the program to open hey.txt and read from it (maybe)
fh = open ("hey.txt","r")

text_hey.close()


