import csv

with open("conditional.csv","r") as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        print(f"Hi! My name is {line[0]}")
        if line[1] == "TRUE":
            print("I live on floor!")
            print(f"I live in room {line[2]}")
        else:
            print("I do not live on floor!")
        print(f"My RIT Email is {line[3]}@rit.edu")