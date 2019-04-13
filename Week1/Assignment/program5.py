#Write a Python program to remove the characters which have odd index values of a given string

var=input("Enter a String: ")
var1 = var[::2] 
print("New String:- %s" %var1)