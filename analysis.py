import csv

def get_highest_gdp(data, year):
    high = float(data[0][year])
    for row in data:
            value = float(row['2020'])
            if value > high:
             high = value
    return high

def get_lowest_gdp(data, year):
    low = float(data[0][year])
    for row in data:
            value = float(row['2020'])
            if value < low:
             low = value
    return low

def get_state_gdp(data, state, year):
 for row in data:
    if row['GeoName'] == state:
        return row[year]


# save each row into a list
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)
        

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print(get_highest_gdp(list_data, '2020'))

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
print(get_lowest_gdp(list_data, '2020'))

#New York GDP for 2020 using "get_state_gdp(list_data,'New York', '2020'"
print (get_state_gdp(list_data,'New York', '2020'))

#New York GDP for 2019 using "get_state_gdp(list_data,'New York', '2019'"
print (get_state_gdp(list_data,'New York', '2019'))

#How much New York droped in GDP from 2019 to 2020
prev = float(get_state_gdp(list_data, "New York", "2019"))
new = float(get_state_gdp(list_data, "New York", "2020"))

print (new - prev)