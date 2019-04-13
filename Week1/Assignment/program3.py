'''
Write a Python program to get a single string from two given strings by user , separated by a space and swap the first 
two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'
'''

var1=input("Enter String number1: ")
var2=input("Enter String number2: ")

var3=var2[:2] + var1[2:] + " " + var1[:2] + var2[2:]
print("New String:- %s" %var3)