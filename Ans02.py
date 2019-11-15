import sys
file_name = 'D:/BABIIII/babiiii/Concordia UN/First Course Introduction to Pathon/Assignment_Lecture_4/Homwork5_Complete/data/complete.csv'
f = open(file_name)
lines = f.readlines()
for line in lines[1:]:
    columns = line.split(',')
    clean_columns = [] # this will contain the correctly-parsed columns
    in_quote = False  
    for x in columns: # we go through the "dirty" columns of data. We will set in_quote to True when we are inside a quote
        if not in_quote:
            clean_columns += [ x ] # we aren't in a quote, we can add the column to the clean ones
            if '"' in x:  # x contains a quote, we will have to handle the next columns differently
                in_quote = True
        else:
            clean_columns[-1] += x  # we are in a quote, we musn't create a new column. Instead, we append the current column to the last one in columns_clean
            if '"' in x:  # this is our closing quote, next column will be out of the quote
                in_quote = False
    try:
        price = int(clean_columns[9])
    except:
        print("Parsing ERROR: ",line)
        sys.exit(1)
    if price >= 50 and price <= 150:
        print(line)