#WAP to insert a string in the middle of a other string.

var=input("Enter a String: ")
length = len(var)
print("Length of String is %s" %length)

var1=input("Enter String to be entered in middle: ")

var2 = var[:int(length/2)] + var1 + var[int(length/2):]
print("New String:- %s" %var2)
