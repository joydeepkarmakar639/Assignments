# Dictionary mapping month numbers to season names
seasons = {
    1: 'Winter',  2: 'Winter',  3: 'Spring',
    4: 'Summer',  5: 'Summer',  6: 'Summer',
    7: 'Monsoon',  8: 'Monsoon',  9: 'Autumn',
    10: 'Autumn', 11: 'Autumn', 12: 'Winter'
}

# Get the month number from the user
month = int(input("Enter the month number (1-12): "))

# Get the season based on the month number
season = seasons.get(month, 'Invalid month number')

# Print the season
if month < 1 or month > 12: print("Invalid month number")
else: print("The season is:", season)
