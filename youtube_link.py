# tells the program that og is the plain link with out any time indicator
og = '''
https://youtu.be/-F6PDE3idKs?list=PLei96ZX_m9sWS2gm1zGqGq6ZzU9T5QSg7&t='''
# tells the program that the time is 385 seconds through the video
time = 385
# tells the program that the link varable is the og and time variables combined, 
# with the time variable coming after the og variable
# str (time) tells python that its ok to turn time into a string
link  = og + str(time)
# tells the program to print the entire link variable 
# (to check if it functionscorrectly)
print (link)
# the modulus (%) divides two integers, and returns with the remainder 
# (if there is one) 
print (12%4)