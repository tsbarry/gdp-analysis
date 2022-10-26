import csv
from re import M

def get_highest_gdp(data, year):
    Maximum = float(row[0][year])
    for row in data:
            val = float(row[year])
            if val > maximum:
             maximum = val
    return maximum
def get_lowest_gdp(data, year):
    pass

# save each row into a list
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)
print(list_data)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"


# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
