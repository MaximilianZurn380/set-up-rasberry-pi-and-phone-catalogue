
file = "telefondata.txt"

import sqlite3

conn = sqlite3.connect('telefonkatalog.db')

cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS persones (
               fornavn TEXT,
               etternavn TEXT,
               telefonnummer TEXT
            )''')

conn.commit()


def showAllPeople():
    cursor.execute("SELECT * FROM persones")
    results = cursor.fetchall()
    if not results:
        print("there are no registered people in the catalogue")
        input("press any key to return to menu ")
        printMenu()
    else:
        print("*********************************"
              "*********************************")
        for persones in results:
            print("* First name: {:15s} Last name: {:15s} Phonenumber: {:8s}".format(persones[0], persones[1], persones[2]))
        print("*********************************"
              "*********************************")
        input("press any key to return to menu ")
        printMenu()


def add_person_to_db(fornavn, etternavn, telefonnummer):
    cursor.execute("INSERT INTO persones (fornavn, etternavn, telefonnummer) VALUES (?, ?, ?)", (fornavn, etternavn, telefonnummer))
    conn.commit()


def remove_person_from_db(fornavn, etternavn, telefonnummer):
    cursor.execute("DELETE FROM persones WHERE fornavn=? AND etternavn=? AND telefonnummer=?", (fornavn, etternavn, telefonnummer))
    conn.commit()


def printMenu():
    print("---------------------Phonus listus---------------------")
    print("1. Add person                                         |")
    print("2. Search for person/number                           |")
    print("3. Show contacts                                      |")
    print("4. Quit                                               |")
    print("-------------------------------------------------------")
    menuchoice = input("input a number to choose an option: ")
    outfoerMenuchoice(menuchoice)


def outfoerMenuchoice(chosenNumber):
    if chosenNumber == "1":
        registerPerson()
    elif chosenNumber == "2":
        searchPerson()
        printMenu()
    elif chosenNumber == "3":
        showAllPeople()
    elif chosenNumber == "4":
        confirmation = input("are you sure? Y/N")
        if (confirmation == "Y" or confirmation == "y"):
            conn.close()
            exit()
        if (confirmation == "N" or confirmation == "n"):
            print("ok")
            printMenu()
    else:
        newTry = input("input a number to choose an option: ")
        outfoerMenuchoice(newTry)


def registerPerson():
    fornavn = input("enter first name: ")
    etternavn = input("enter last name: ")
    telefonnummer = input("enter phonenumber: ")

    add_person_to_db(fornavn, etternavn, telefonnummer)

    print("{0} {1} are registered with phonenumber {2}".format(fornavn, etternavn, telefonnummer))
    input("input any key to return to menu: ")
    printMenu()

def searchPerson():
    print("1. search first name")
    print("2. search last name")
    print("3. search phone number")
    print("4. back to main menu")
    searchfield = input("input a number to choose an option: ")
    if searchfield == "1":
        name = input("First name: ")
        findPerson("first name", name)
    elif searchfield == "2":
        name = input("Last name: ")
        findPerson("last name", name)
    elif searchfield == "3":
        phnnumber = input("Phonenumber: ")
        findPerson("phonenumber", phnnumber)
    elif searchfield == "4":
        printMenu()
    else:
        print("unworthy choise. choose a worthy number (1-4)")
        searchPerson()


def findPerson(typeSearch, searchText):
    if typeSearch == "first name":
        cursor.execute("SELECT * FROM persones WHERE fornavn=?", (searchText,))
    elif typeSearch == "last name":
        cursor.execute("SELECT * FROM persones WHERE etternavn=?", (searchText,))
    elif typeSearch == "phonenumber":
        cursor.execute("SELECT * FROM persones WHERE telefonnummer=?", (searchText,))

    results = cursor.fetchall()

    if not results:
        print("your phone catalogue is empty, looser")
    else:
        for personers in results:    
                print("{0} {1} has phonenumber {2}".format(personers[0], personers[1], personers[2]))


printMenu()