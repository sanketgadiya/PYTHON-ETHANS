# Program - Enter student info and show results as per question
'''
print("Enter Student detail - Full Name ( First Name and Last Name) , Age & Class")

print("Student1")
fname = input("First Name:")
lname = input("Last Name:")
age = input("Age:")
clas = input("Class:")
list_s1 = [fname,lname,age,clas]
#print(list_s1)
#print('#'*20)
print("Student2")
fname = input("First Name:")
lname = input("Last Name:")
age = input("Age:")
clas = input("Class:")
list_s2 = [fname,lname,age,clas]
##print(list_s2)
#print('#'*20)
print("Student3")
fname = input("First Name:")
lname = input("Last Name:")
age = input("Age:")
clas = input("Class:")
list_s3 = [fname,lname,age,clas]
#print(list_s3)
#print('#'*20)
print("Student4")
fname = input("First Name:")
lname = input("Last Name:")
age = input("Age:")
clas = input("Class:")
list_s4 = [fname,lname,age,clas]
#print(list_s4)
#print('#'*20)
print("Student5")
fname = input("First Name:")
lname = input("Last Name:")
age = input("Age:")
clas = input("Class:")
list_s5 = [fname,lname,age,clas]
#print(list_s5)
print('#'*20)
'''
student_list = [['sanket', 'jain', '23', '12'], ['chinal', 'jain', '32', '23'], ['maahir', 'jain', '32', '2'], ['sanket', 'gadita', '32', '23'], ['vijat', 'asas', '23', '12']]
#student_list1 = [list_s1,list_s2,list_s3,list_s4,list_s5]
print(student_list)

print('#'*50)
print("Total Students:- %s" %len(student_list))
student_name = student_list[0:][0]
print(student_name)