import sys
file_name = sys.argv[1] # 'airbnb/Complete.csv'
price_min = int(sys.argv[2])
price_max = int(sys.argv[3])
Seperater=str(sys.argv[4])
R=str(sys.argv[5])
f = open(file_name)
lines = f.readlines()
in_quote = False
for line in lines[1:]: # here we only read the first 20 lines to shorten display
    columns = line.split(Seperater)
    if not in_quote: # if in_quote is True, we are still parsing the previous line, there was a newline between quotes
        clean_columns = [] # this will contain the correctly-parsed columns
    for x in columns: # we go through the "dirty" columns of data. We will set in_quote to True when we are inside a quote
        clean_x = x.replace(R, '') # we remove the "escaped" quotes from x
        n_quotes = clean_x.count('"')
        if not in_quote:
            clean_columns += [ clean_x ] # we aren't in a quote, we can add the column to the clean ones
            if n_quotes % 2 != 0:  # x contains an odd number of quotes, we will have to handle the next columns differently
                in_quote = True
        else:
            clean_columns[-1] += clean_x  # we are in a quote, we musn't create a new column. Instead, we append the current column to the last one in columns_clean
            if n_quotes % 2 != 0:  # this is our closing quote, next column will be out of the quote
                in_quote = False
    if not in_quote:
        # line parsing is finished, we can print the price
        try:
            price = int(clean_columns[9])
        except:
            print("Parsing ERROR: ",line)
            sys.exit(1)
        if price >= price_min and price <= price_max:
            print(line)
