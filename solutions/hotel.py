def print_header():
	print "#"*30+"\n          MENU         \n"+ "#"*30

def print_menu_item(item,price,total_gap=30):
	total_char = len(item) + len(str(price)) + 2
	h_needed = total_gap - total_char
	print item + " " +"-"*h_needed + " " + str(price)
	
def print_menu(menu_dict=''):
	print_header()
	for item in menu_dict:
		print_menu_item(item,menu_dict[item])
	
def main():		
	dict1 = {'Rice':40,'Roti':13,'Curry':450,'Papad':45}
	print_menu(dict1)
	all_choice = []
	print " "
	while True:
		choice = raw_input("Enter the item to order else 'D' for done :")
		if choice == 'D':
			break
		elif choice not in dict1:
			print "Not available in menu"
			print "  "
		else:
			all_choice.append(choice)
	bill = 0
	for c in all_choice:
		if 'Roti' in all_choice and 'Curry' in all_choice:
			bill = bill + dict1[c]
		else:
			print "\n \n Your order is incomplete \n \n"
			return
	print "\n \n Total Bill : %s" %bill
		
main()
		
		
		
		