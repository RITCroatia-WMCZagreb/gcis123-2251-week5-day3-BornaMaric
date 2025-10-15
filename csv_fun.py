
#Reading advances CSV (has """ inside) - do not use simple file reader
def names_and_addresses_01(filename:str):
    with open(filename) as csv_file:
        next(csv_file) #skipping first line
        for line in csv_file:
            #print(line)
            fields = line.split(",")
            print("name:",fields[0]," adress:",fields[1])


#Advanced CSV reader
import csv
def names_and_addresses_02(filename:str):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            print("name:",row[0]," adress:",row[1])





def main():
    #names_and_addresses_01("data/full_grades_010.csv")
    names_and_addresses_02("data/full_grades_010.csv")

