def writeee():
    with open("file.txt", "w") as f:
     f.write("Hello World\n")

    with open("file.txt", "r") as f:
     content = f.read()
     print(content)

    with open("mani.txt","w") as f :
        f.write("Hello Mani\n")
    
    with open("mani.txt","a") as f :
        f.write("How are you?")

    with open("mani.txt","r") as f :
        print(f.read())

def csvfor():
    with open("details.csv") as f :
        for line in f :
            if age >= 20: 
                print(f.read())



def tryexcept():
       try : 
          with open("missing.txt","r") as f :
             print(f.read())
       except FileNotFoundError :
             print ("file not found")
        
writeee()
tryexcept()



import csv

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Mani", 25])
    writer.writerow(["Ravi", 30])

with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import json

person = {
    "name": "Mani",
    "age": 25,
    "skills": ["Python", "Testing"]
}

with open("person.json", "w") as f:
    json.dump(person, f, indent=2)

with open("person.json", "r") as f:
    data = json.load(f)
    print(data)
    print(data["skills"])