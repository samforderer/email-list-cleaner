import csv
import dns.resolver 
import re 
import itertools
import time 

# function definitions 
    
def syntaxCheck(email):
    regex = '^[a-z0-9]+[._-]?[a-z0-9]+[@][a-z0-9]+[._-]?[a-z0-9]+\.[a-z]{2,3}$' 
    match = bool(re.match(regex, email))
    return match


def dnsCheck(email):
    syntaxCheck(email)
    splitAddress = email.split('@')
    domain = splitAddress[1]
    print(domain)
    return True


def validate_email(email_address):
    # Nested checks so if it doesn't pass it returns false would be best
    # 1. check syntax regex 
    if syntaxCheck(email_address):
        #2. MX record check
        if dnsCheck(email_address):
            return True


# READ FILE and APPEND TO LIST 
def readfile(in_file, startrow, endrow, index):
    # open file
    with open(f"{in_file}.csv", 'r') as csvfile:

        #initialize list to store emails in
        emailList = []

        # define reader object
        csv_reader = csv.reader(csvfile)

        # loop through
        for line in itertools.islice(csv_reader, startrow, endrow):
            emailList.append(line[index])
            print(line[index])
            time.sleep(0.1)

        return emailList
        


# reads the list from readfile and adds them to new specified CSV file if the email is valid
def writefile(out_file, emailList):
    with open(f'{out_file}.csv', 'a', newline='') as file:

        writer = csv.writer(file)

        for i in range(0, len(emailList)):
            writer.writerow([f'{emailList[i]}'])
        


# main menu to select which option 
def menu():

    choice = ''
    text = 'Welcome to: Email Validation Tools (Select Option)'
    text2 = '1. Read List \n2. Validate List \n3. Write File \n'
    emailList = []
    separator = "-"*50 

    while True:
        print(separator)
        print(text)
        if emailList:
            print("List Loaded: ", len(emailList))
        print(separator)
        choice = input(text2)

        # read file 
        if choice == '1':
            
            # get parameters for processing the CSV file 
            inFile = input("Enter file name: ")
            
            startRow = int(input("What row to start processing from: "))
            endRow = int(input("Enter number of rows to validate: ")) + 1
            startIndex = int(input("Enter column number: "))
            print()
            try:
                emailList = readfile(inFile, startRow, endRow, startIndex) 
            except:
                print("File not Found")

        # Check syntax
        elif choice == '2':
            if emailList:
                count = 1
                for email in emailList:
                    print(count, "Processing...")
                    time.sleep(0.3)
                    if validate_email(email):
                        print("This email has good syntax")
                    else:
                        print("Error: This email has bad syntax")
                    time.sleep(0.5)
                    count += 1 
            else:
                print(separator)
                print("You must load data into the list before validating!")
                time.sleep(0.4)

        elif choice == '3':
            if emailList: 
                outFile = input("Enter Name of output file: ")
                writefile(outFile, emailList)
            else:
                print("You must load data into the list before writing out")

        elif choice == 'quit':
            break
        else:
            print("invalid input")


# MAIN PROGRAM 
menu()
         
