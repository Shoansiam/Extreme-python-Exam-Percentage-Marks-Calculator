#Gpa calculator

# Total marks of exam was stored on ntotal
ntotal = 500
# Your English exam result will stored on Eng
Eng = input("Your Achived English Mark is: ")
# Your math exam result will stored on math
math = input("Your Achived Math Mrks is: ")
# Your accounting result will stored on accounting
accounting = input("enter your accounting marks: ")
# your finance marks will stored on finance 
finance = input("enter your finance marks: ")
# Your computer marks will stored on computer
computer = input("Enter Your computer marks: ")

#Student Achived total number will stored on ototal
ototal = int(Eng)+int(math)+int(accounting)+int(finance)+int(computer)
print("Your total number is :",ototal)

# ntotal and ototal divine answer two proccess make percentage
divine = ototal/ntotal
# The percentage variable is a normal magic is will create percentage number
percentage = divine*100
print("CONGRATULATION! You are achived"+str(percentage)+" %"+" of number")
