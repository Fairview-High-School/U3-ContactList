###################################################################
#  Contact List
#  AP Computer Science Principles
#
#  Your name: ____________________
#
#  Look for the lines marked  # TODO  - those are the parts you write.
#  Everything else is provided. Read it carefully: you will use it.
###################################################################

import turtle
from tkinter import messagebox

screen = turtle.Screen()
screen.setup(480, 360)
screen.title("Contact List")

contactList = []     # every contact in the program lives in this ONE list

# ---------------------------------------------------------------
# Images  (all five .gif files must be in the same folder as this file)
# ---------------------------------------------------------------
addContactImage = "addContact.gif"
deleteContactImage = "deleteContact.gif"
findContactImage = "findContact.gif"
clearListImage = "clearList.gif"
screen.register_shape(addContactImage)
screen.register_shape(deleteContactImage)
screen.register_shape(findContactImage)
screen.register_shape(clearListImage)
screen.bgpic("contactList.gif")

# Button turtles
addButton = turtle.Turtle(shape=addContactImage)
deleteButton = turtle.Turtle(shape=deleteContactImage)
findButton = turtle.Turtle(shape=findContactImage)
clearButton = turtle.Turtle(shape=clearListImage)


###################################################################
#  POPUP HELPERS  (provided - these replace Python's input() and print())
###################################################################

def input(prompt, title="Contact List"):
    """Like INPUT() on the AP reference sheet: shows a popup with a text box
    and returns what the user typed.
    Unlike Python's usual input(), it returns None if the user clicks Cancel."""
    return screen.textinput(title, prompt)


def display(message, title="Contact List"):
    """Like DISPLAY() on the AP reference sheet: shows a popup message
    with an OK button."""
    messagebox.showinfo(title, message)


def confirm(question, title="Contact List"):
    """Shows a Yes/No popup. Returns True for Yes, False for No."""
    return messagebox.askyesno(title, question)


###################################################################
#  PART 1 - THE CONTACT ADT ABSTRACTION
#
#  A contact is stored as a list of 5 strings:
#       [first name, last name, phone, email, address]
#  The rest of the program NEVER uses contact[0], contact[1], ...
#  It only uses the functions below.
###################################################################

def makeContact(first, last, phone, email, address):
    return [first, last, phone, email, address]


def getFirstName(contact):
    return contact[0]


def getLastName(contact):
    # TODO: return the contact's last name
    return ""


def getPhone(contact):
    # TODO: return the contact's phone number
    return ""


def getEmail(contact):
    # TODO: return the contact's email address
    return ""


def getAddress(contact):
    # TODO: return the contact's mailing address
    return ""


def describe(contact):
    """Return ONE string with all of a contact's information,
    on separate lines, like this:

        Ada Lovelace
        Phone: 555-0100
        Email: ada@example.com
        Address: 12 Analytical Way

    Hint: "\\n" inside a string starts a new line.
    Use the get... functions, not contact[0], contact[1], ...
    """
    # TODO
    return ""


###################################################################
#  PART 2 - SEARCHING THE LIST
###################################################################

def findMatches(name):
    """Return a NEW list of every contact in contactList whose first name
    OR last name contains name. Ignore upper/lower case, so "lov" matches
    "Lovelace". If nothing matches, return an empty list [].

    Hints:  "lov" in "lovelace"   evaluates to True
            "Lovelace".lower()    evaluates to "lovelace"
    """
    matches = []
    # TODO: use a loop and an if statement to fill in matches
    return matches


###################################################################
#  PART 3 - BUTTON HANDLERS
#  (x, y) is where the button was clicked. You do not need to use them.
###################################################################

def addContactHandler(x, y):
    # Provided: ask the five questions, stopping if the user clicks Cancel.
    answers = []
    for prompt in ["First name:", "Last name:", "Phone number:",
                   "Email address:", "Mailing address:"]:
        answer = input(prompt, "Add Contact")
        if answer is None:         # the user clicked Cancel
            return
        answers.append(answer)
    first, last, phone, email, address = answers

    # TODO: 1. make a new contact using makeContact
    # TODO: 2. add it to the end of contactList
    # TODO: 3. save the file
    # TODO: 4. display a popup saying the contact was added


def findContactHandler(x, y):
    name = input("Enter first or last name:", "Find Contact")
    if name is None:
        return

    # TODO: call findMatches(name)  store in a variable 
    # TODO: if there are no matches, display "No contacts found"
    # TODO: otherwise, display each matching contact in a popup (use describe) and use a for loop


def deleteContactHandler(x, y):
    name = input("Enter first or last name of the contact to delete:", "Delete Contact")
    if name is None:
        return

    # TODO: call findMatches(name)
    # TODO: if there are no matches, display "No contacts found"
    # TODO: otherwise, for each match:
    #           ask (with confirm) whether to delete it, showing describe(match)
    #           if Yes, remove it from contactList
    # TODO: save the file, then display how many contacts were deleted


def clearListHandler(x, y):
    # TODO: use confirm to ask "Are you sure you want to delete the ENTIRE list?"
    # TODO: if Yes, empty contactList, save the file, and display "Cleared."
    #       otherwise, display "Cancelled."
    # Hint: contactList.clear() empties the list.
    pass


###################################################################
#  SAVING AND LOADING  (provided - do not change)
#  Contacts are kept in contactList.txt, one contact per line,
#  with a tab between each piece.
###################################################################

FILE_NAME = "contactList.txt"


def saveFile():
    contactFile = open(FILE_NAME, "w")
    for c in contactList:
        pieces = [getLastName(c), getFirstName(c), getPhone(c), getEmail(c), getAddress(c)]
        contactFile.write("\t".join(pieces) + "\n")
    contactFile.close()


def loadFile():
    try:
        contactFile = open(FILE_NAME, "r")
    except FileNotFoundError:      # first run: no file yet, start empty
        return
    for line in contactFile:
        pieces = line.strip("\n").split("\t")
        if len(pieces) == 5:
            last, first, phone, email, address = pieces
            contactList.append(makeContact(first, last, phone, email, address))
    contactFile.close()


###################################################################
#  SETUP AND MAIN  (provided)
###################################################################

def setup():
    screen.tracer(0)
    for button, y in [(addButton, 100), (deleteButton, 50), (findButton, 0), (clearButton, -50)]:
        button.penup()
        button.goto(150, y)
    screen.update()
    addButton.onclick(addContactHandler)
    deleteButton.onclick(deleteContactHandler)
    findButton.onclick(findContactHandler)
    clearButton.onclick(clearListHandler)


setup()
loadFile()
turtle.mainloop()
