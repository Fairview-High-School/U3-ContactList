import turtle

screen = turtle.Screen()

contactList = []

screen.setup(480,360)

#Images
addContactImage = "addContact.gif"
screen.register_shape(addContactImage)
deleteContactImage = "deleteContact.gif"
screen.register_shape(deleteContactImage)
findContactImage = "findContact.gif"
screen.register_shape(findContactImage)
clearListImage = "clearList.gif"
screen.register_shape(clearListImage)
contactListBackground = "contactList.gif"

#Button Turtles
addContact = turtle.Turtle()
addContact.shape(addContactImage)
deleteContact = turtle.Turtle()
deleteContact.shape(deleteContactImage)
findContact = turtle.Turtle()
findContact.shape(findContactImage)
clearList = turtle.Turtle()
clearList.shape(clearListImage)
#set background image
screen = turtle.Screen()
screen.bgpic(contactListBackground)

def setup():
   turtle.tracer(0,0)
   addContact.penup()
   addContact.goto(150,100)
   addContact.left(90)
   deleteContact.penup()
   deleteContact.goto(150,50)
   deleteContact.left(90)
   findContact.penup()
   findContact.goto(150,0)
   findContact.left(90)
   clearList.penup()
   clearList.goto(150,-50)
   clearList.left(90)
   turtle.update()
   addContact.onclick(addContactHandler)
   deleteContact.onclick(deleteContactHandler)
   findContact.onclick(findContactHandler)
   clearList.onclick(clearListHandler)
   
########################################################
#Contact ADT
def contact(fName, lName, phone, email, address):
  return [fName, lName, phone, email, address]
  
def getFirstName(contact):
  return contact[0]

def getLastName(contact):
  return 
  
def getPhone(contact):
  return 

def getEmail(contact):
  return 

def getAddress(contact):
  return 


###################################
#Button Handlers
def addContactHandler(x,y):
  #input contact info
  first = input("First Name: ")
  last = input("Last Name: ")
  phone = input("Phone number: ")
  email = input("Email address: ")
  address = input("Mailing address: ")
  
  newContact = contact(first, last, phone, email, address)
  #add line here to append the new contact to the contactList
  
  #add line here to save the file
	
def deleteContactHandler(x,y):
	#enter name of person to find
  name = input("Enter first or last name of the contact to delete: ")
  
  #search for that contact
  for contact in contactList:
    if name.lower() in getFirstName(contact).lower() or name.lower() in getLastName(contact).lower():
      #display the contact info for that contact
      print (getFirstName(contact) + " " + getLastName(contact))
      print ("Phone Number: " +  getPhone(contact))
      print ("Email: " + getEmail(contact))
      print ("Address: " + getAddress(contact))
      
      answer = input("Do you want to delete this contact?(y/n): ")
      if answer == "y":
        #add line here to remove the contact from the contact list
        #add line here to save the file
        print("Contact Deleted")
	
def findContactHandler(x,y):
  #enter name of person to find
  name = input("Enter first or last name: ")
  
  #search for that contact
  for contact in contactList:
    if name.lower() in getFirstName(contact).lower() or name.lower() in getLastName(contact).lower():
      #display the contact info for that contact
      #add print statements to print each part of the contact
      
def clearListHandler(x,y):
  global contactList
  answer = input("Are you sure you want to delete the entire list (y/n): ")
  if answer == "y":
    contactList = []
    saveFile()
    print("Cleared")
  else:
    print("Cancelled")

###################################
#Load and Save Data

def saveFile():
  contactFile = open("contactList.txt", "w")
  for contact in contactList:
    contactFile.write(getLastName(contact) + "\t" + getFirstName(contact) + "\t")
    contactFile.write(getPhone(contact) + "\t" + getEmail(contact) + "\t" )
    contactFile.write(getAddress(contact))
    contactFile.write("\n")
  contactFile.close()
  
def loadFile():
  contactFile = open("contactList.txt", "r")
  for line in contactFile:
    con = line.strip("\n").split("\t")
    if len(con) > 1:
      lastName = con[0]
      firstName = con[1]
      phone = con[2]
      email = con[3]
      address = con[4]
      newContact = contact(firstName, lastName, phone, email, address)
      contactList.append(newContact)
  contactFile.close()

###################################
#MAIN SCRIPT
setup()
loadFile()

turtle.mainloop()













