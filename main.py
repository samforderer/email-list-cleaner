import csv
import py3-validate-email


def readfile(in_file):
    # open file
    with open(f"{in_file}.csv", 'r') as csvfile:
        # define reader object
        csv_reader = csv.reader(csvfile)
        # skip header line
        next(csv_reader)
        # loop through
        for line in csv_reader:
            emailList.append(line[0])


def validate_email_addr(email_address):

    is_valid = validate_email(
        email_address='example@example.com',
        check_format=True,
        check_blacklist=True,
        check_dns=True,
        dns_timeout=10,
        check_smtp=True,
        smtp_timeout=10,
        smtp_helo_host='my.host.name',
        smtp_from_address='my@from.addr.ess',
        smtp_skip_tls=False,
        smtp_tls_context=None,
        smtp_debug=False,
        address_types=frozenset([IPv4Address, IPv6Address]))


def writefile(out_file):
    with open(f'{out_file}.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(emailList)):
            if validate_email_addr(emailList[i]):
                writer.writerow([f'{emailList[i]}'])
            else:
                print("error validating")


# Main Program
# file names for input and output
inFileName = input("Enter file name: ")
outFileName = input("Enter Name of output file: ")

# initialize list
emailList = []

print('beginning email reading')
readfile(inFileName)
print('email reading complete..')

print('beginning email writing and validating')
writefile(outFileName)

