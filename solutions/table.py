num = 10
reversed_at = 10
list1 = []

if num == reversed_at:
	list1 = range(11)
elif (num%2 == 0 and num < reversed_at) or (num%2 != 0 and num > reversed_at):
	list1 = range(0,11,2)
elif (num%2 == 0 and num > reversed_at) or (num%2 != 0 and num < reversed_at):
	list1 = range(1,10,2)
else:
	print "ERROR"

print "-"*20
for i in list1:
	if i == 3:
		continue
	elif i == 6:
		break
	print "%s * %s = %s" %(num,i,num*i)
print "-"*20

