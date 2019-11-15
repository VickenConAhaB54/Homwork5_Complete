import sys
file_name = 'D:/BABIIII/babiiii/Concordia UN/First Course Introduction to Pathon/Assignment_Lecture_4/Homwork5_Complete/data/complete.csv'
f = open(file_name)
lines = f.readlines()
for line in lines[1:]:
    columns = line.split(',')
    try:  
        price = int(columns[9])
    except:
        print("Parsing ERROR: ",line)
        sys.exit(1)  # this stops the program
    if price >= 100 and price <= 150:
        print(line)