db = {}
while True:
	print "#"*40
	print "Enter your choice"
	print "(1) Enter information"
	print "(2) Query information"
	print "(3) Exit "
	choice = int(raw_input("Enter your choice:"))
	if choice == 1:
		sname = raw_input("Enter Student name:" )
		sclass = raw_input("Enter Student class:" )
		ssection = raw_input("Enter Student class section:" )
		sid = int(raw_input("Enter Students school Roll number:" ))
		s_maths_marks = int(raw_input("Enter Student Maths marks:"))
		s_eng_marks = int(raw_input("Enter Student English marks:"))
		if db.has_key(sid):
			print "[ERROR] : Student Information Already Present"
		else:
			marks = {'maths' : s_maths_marks,'English': s_eng_marks}
			db_temp = {sid :{'name'   : sname,
							 'class'  : sclass,
							 'section':	ssection,
							 'marks'  : marks}
						}
			db.update(db_temp)
	elif choice == 2 :
			#print db
		sid = int(raw_input("Enter student school Roll no :"))
		if not db.has_key(sid):
			print "[ERROR] : INVALID ROLL NUMBER"
		else:
			print ""
			print "#"*30
			print " %s RESULT" %db[sid]['name']
			print "#"*30
			print "MATHS        :       %s" %db[sid]['marks']['maths']
			print "English      :       %s" %db[sid]['marks']['English']
			print "#"*30
			print ""
	elif choice == 3 :
		print "BYE BYE"
		break
	else:
		print "[ERROR] : INVALID CHOICE"
