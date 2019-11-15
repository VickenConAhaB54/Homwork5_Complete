import sys
file_name = 'D:/BABIIII/babiiii/Concordia UN/First Course Introduction to Pathon/Assignment_Lecture_4/Homwork5_Complete/data/complete.csv'
f = open(file_name)
lines = f.readlines()
for line in lines[1:]:
    columns = line.split(',')
    R_columns = [] # this will contain the correctly-parsed columns
    for x in columns:
       R_columns += [ x ]
       price = int(R_columns[9])
       if price >= 100 and price <= 150:
          print(line)  