print "Welcome to Contacts Manager!\n\n"

def getContacts():
	try:
		file = open('contacts.csv', 'r')
		contacts = file.readlines()
		return contacts
	except Exception as e:
		raise e
		return None
	finally:
		file.close()

def showContacts():
	print "\n\nContacts in your PyContacts : "
	print "___________________________________\n\n"
	contacts = getContacts()
	for contact in contacts:
		name, number = contact.split(',')
		print name + " - " + number + "\n"
	print "___________________________________\n\n"

def createContact(name, number):
	status = False
	try:
		file = open('contacts.csv', 'a')
		file.write("\n"+name+","+str(number))
		status = True
	except Exception as e:
		raise e
	finally:
		file.close()
	return status

def searchContact(name,number=None):
	contacts = getContacts()
	for contact in contacts:
		cname, cnumber = contact.split(",")
		if cname is name or cnumber is number:
			return [cname, cnumber]
	return False

if __name__ == "__main__":
	print "Welcome to PyContacts - the Contact Manager made in Python!"
	while True:
		c = raw_input("Enter the command to [a]dd, [s]earch, [d]isplay contacts or [q]uit : ")
		if c == "a" : 
			name, number = raw_input("Enter the name of the contact: "), raw_input("Enter the number of contact: ")
			print "Successfully created contact!\n" if createContact(name,number) else "Couldn't create the contact!\n"
		elif c == "s":
			name = raw_input("Enter the name of the contact you want to search: ")
			contacts = searchContact(name)
			if contacts != None:
				print "\nFound the contact!"
				print "Name: " + contacts[0] + " \t Number: " + contacts[1] + " \n\n"
			else :
				print "Couldn't find the contact!\n"
		elif c == "d":
			showContacts()
		else :
			break
	print "\nThanks for using PyContacts!\n"
	exit()