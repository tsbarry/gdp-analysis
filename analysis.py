import csv

def get_highest_gdp(data, year):
    high = float(data[0][year])
    State_name = str(data[0]['GeoName'])
    for row in data:
            value = float(row[year])
            if value > high:
             high = value
             State_name = row['GeoName'] 
    return State_name #this will return the state with the highest gdp
    #return high(if we wanted to return the highest gdp in number)

def get_lowest_gdp(data, year):
    low = float(data[0][year])
    State_name = str(data[0]['GeoName'])
    for row in data:
            value = float(row[year])
            if value < low:
             low = value
             State_name = row['GeoName'] 
    return State_name #this will return the state with the highest gdp
    #return low(this will return the lowest numerical gdp)

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
# this code appends all rows as dictionaries to list_data
        

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