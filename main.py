import csv
import dns.resolver 
import re 
import itertools
import time 

# function definitions 
    

def syntaxCheck(email):
    regex = '^[a-z0-9]+[._-]?[a-z0-9]+[@][a-z0-9]+[.][a-z]{2,3}$' 
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


# reads the list from readfile and adds them to new specified CSV file if the email is valid
def writefile(out_file):
    with open(f'{out_file}.csv', 'a', newline='') as file:

        writer = csv.writer(file)
        for i in range(0, len(emailList)):
            print(f'starting {i}') 
            is_valid = validate_email(emailList[i])
            if is_valid:
                writer.writerow([f'{emailList[i]}'])
                print(valid)
            else:
                print("not adding to list")
        
        return emailList


# main menu to select which option 
def menu():
    choice = ''
    text = '\nEMAIL TOOLS (Select Option)'
    text2 = '1. Read List \n2. Check Syntax \n3. Write File \n'
    
    menu_options = ('1', '2', '3', 'q')
    while True:
        
        print(text)
        print()
        choice = input(text2)

        # read file 
        if choice == '1':
            
            # get parameters for processing the CSV file 
            inFile = input("Enter file name: ")
            
            startRow = int(input("What row to start processing from: "))
            endRow = int(input("Enter number of rows to validate: "))
            startIndex = int(input("Enter column number: "))

            readfile(inFile, startRow, endRow, startIndex) 

        # Check syntax
        elif choice == '2':                    
            email = input("REGEX: Enter String: \n")
            print("Processing...")
            time.sleep(2)
            if validate_email(email):
                print("This email has good syntax")
            else:
                print("Error: This email has bad syntax")
            time.sleep(0.5)

        elif choice == '3':
            if emailList: 
                outFile = input("Enter Name of output file: ")
                writefile(outFile)
            else:
                print("You must load data into the list before writing out")

        elif choice == 'quit':
            break


# MAIN PROGRAM 

#initialize the list data 
emailList=[]

menu()
         
# create menu that has read file option that allows you to read a specified amount of emails from a csv and add it to a list, you can then decide how you want to process the data 
