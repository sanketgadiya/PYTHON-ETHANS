 #Write a Python program to change a given string to a new string where all the even position characters are in 
 # starting and all odd position characters are in end.

var=input("Enter a String: ")
var1 = var[1::2] + var[::2]
print("New String:- %s" %var1)