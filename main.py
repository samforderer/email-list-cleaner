import csv
import itertools
from validate_email import validate_email


def readfile(in_file, startrow, endrow):
    # open file
    with open(f"{in_file}.csv", 'r') as csvfile:
        # define reader object
        csv_reader = csv.reader(csvfile)
        # loop through
        for line in itertools.islice(csv_reader, startrow, endrow):
            emailList.append(line[2])
            print(line[2])

    
def writefile(out_file):
    with open(f'{out_file}.csv', 'a', newline='') as file:

        writer = csv.writer(file)
        for i in range(0, len(emailList)):

            valid = validate_email(email_address=emailList[i])

            if valid:
                writer.writerow([f'{emailList[i]}'])
                print(valid)

            else:
                print("error validating")


# Main Program
# file names for input and output
inFileName = input("Enter file name: ")
outFileName = input("Enter Name of output file: ")
startRow = int(input("What row to start processing from: "))
endRow = int(input("Enter number of rows to validate: "))

# initialize list
emailList = []


# function calls
readfile(inFileName)

writefile(outFileName, startRow, endRow)

