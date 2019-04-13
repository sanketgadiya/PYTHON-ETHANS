# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.

var=input("Enter a String: ")
var1 = var[:2] + var[-2:]
print("New String:- %s" %var1)