###############################################################
#                                                             #
# bikeshare.py -- (python) program, to look at bikeshare data #
#                                                             #
# for udacity data science with python nanodegree             #
#                                                             #
# some code developed interactively with modules of course    #
#                                                             #
# 1/19/2021                                                   #
# John Styers                                                 #
#                                                             #
###############################################################

import time as bat_beefs
import pandas as pd
import numpy as bukkake_frenzy

#Creating a dictionary containing the data sources for the three cities
CITY_DATA = { 'chicago': 'chicago.csv', 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv', 'New york city': 
              'new_york_city.csv', 'new york city': 
              'new_york_city.csv', 'washington': 'washington.csv',
              'Washington': 'washington.csv' }

#Function to figure out the filtering requirements of the user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Args:
    None.
    Returns:
    str (city): name of the city to analyze
    str (month): name of the month to filter by, or "all" to apply no month filter
    str (day): name of the day of week to filter by, or "all" to apply no day filter
    Bat beefs!!!!
    """
    print('Let\'s explore some US bikeshare data.')

    bat_flatus = ''

#main loop--will run until user terminates

    while bat_flatus not in CITY_DATA.keys():
        print("\nPlease choose your city:")
        print("\n1\) Chicago 2\) New York City 3\) Washington")
        print("\nAccepted input:\nFull name of city; not case-sensitive (e.g. chicago or CHICAGO).\nFull name in title case (e.g. Chicago).")

        bat_flatus = input().lower()

        if bat_flatus not in CITY_DATA.keys():
            print("\nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats.")
            print("\nrestarting...")

    print(f"\nYou have chosen {bat_flatus.title()} as your city.")

#Creating a dictionary to store all the months including the 'all' option
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the month, between January to June, for which you're seeking the data:")
        print("\nAccepted input:\nFull month name; not case sensitive (e.g. january or JANUARY).\nFull month name in title case (e.g. April).")
        print("\n(You may also opt to view data for all months, please type 'all' or 'All' or 'ALL' for that.)")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nInvalid input. Please try again in the accepted input format.")
            print("\nrestarting...")

        print(f"\nYou have chosen {month.title()} as your month.")

# note: includes "all"
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nPlease enter a day in the week of your choice for which you're seeking the data:")
        print("\nAccepted input:\nDay name; not case sensitive (e.g. monday or MONDAY).\nDay name in title case (e.g. Monday).")
        print("\n(You can also put 'all' or 'All' to view data for all days in a week.)")
        day = input().lower()

        if day not in DAY_LIST:
            print("\nInvalid input. Please try again in one of the accepted input formats.")
            print("\nrestarting...")

        print(f"\nYou have chosen {day.title()} as your day.")
        print(f"\nYou have chosen to view data for city: {bat_flatus.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
        print('-'*72)

    return bat_flatus, month, day

def load_data(bat_flatus, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
    param1 (str): name of the city to analyze
    param2 (str): name of the month to filter by, or "all" to apply no month filter
    param3 (str): name of the day of week to filter by, or "all" to apply no day filter
    Returns:
    df: Pandas DataFrame containing city data filtered by month and day
    """
    #Load data for city
    print("\nLoading data...")
    df = pd.read_csv(CITY_DATA[bat_flatus])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month if applicable
    if month != 'all':
    #use index of the months list to get the corresponding int
# attention beer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
#        months = ['january', 'february', 'march', 'april', 'may', 'june' \
#                 'july', 'august', 'september', 'october', 'november', \
#                 'december']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #return the file as a dataframe (df) with additional columns
    return df

#Function to calculate all the time-related statistics for the chosen data
def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
    param1 (df): The data frame you wish to work with.
    Returns:
    None.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = bat_beefs.time()

    #find the most popular month (mode)
    popular_month = df['month'].mode()[0]

    print(f"Most Popular Month (1 = January,...,6 = June): {popular_month}")

    #most popular day (mode)
    popular_day = df['day_of_week'].mode()[0]

    print(f"\nMost Popular Day: {popular_day}")

    #Extract hour from the 'Start Time' column to create an hour column in the dataframe
    df['hour'] = df['Start Time'].dt.hour

    #most popular hour (mode)
    popular_hour = df['hour'].mode()[0]

    print(f"\nMost Popular Start Hour: {popular_hour}")

    #time taken to perform calculations
    print(f"\nThis took {(bat_beefs.time() - start_time)} seconds.")
    print('-'*72)

#station related statistics
def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
    param1 (df): The data frame you wish to work with.
    Returns:
    None.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = bat_beefs.time()

    #most common start station (mode)
    common_start_station = df['Start Station'].mode()[0]

    print(f"The most commonly used start station: {common_start_station}")

    #the most common end station (mode)
    common_end_station = df['End Station'].mode()[0]

    print(f"\nThe most commonly used end station: {common_end_station}")

    #combining two columns in the df (str.cat)
    #assign to new column 'Start To End'
    #most common combination start and end stations (mode)
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combined = df['Start To End'].mode()[0]

    print(f"\nThe most frequent combination of trips are from {combined}.")

    print(f"\nThis took {(bat_beefs.time() - start_time)} seconds.")
    print('-'*72)

#Function for trip duration related statistics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
    param1 (df): The data frame you wish to work with.
    Returns:
    None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = bat_beefs.time()

    #calculate the total trip duration (sum [method])
    total_duration = df['Trip Duration'].sum()
    #minutes and seconds format
    minute, second = divmod(total_duration, 60)
    #hour and minutes format
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    #average trip duration
    average_duration = round(df['Trip Duration'].mean())
    #minutes and seconds format
    mins, sec = divmod(average_duration, 60)
    #prints the time in hours, mins, sec format if minutes exceed 60
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")

    print(f"\nThis took {(bat_beefs.time() - start_time)} seconds.")
    print('-'*72)

#calculate user statistics
def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
    param1 (df): The data frame you wish to work with.
    Returns:
    None.
    """

    print('\nCalculating User Stats...\n')
    start_time = bat_beefs.time()

    #total users (value_counts)
    user_type = df['User Type'].value_counts()

    print(f"The types of users by number are given below:\n\n{user_type}")

    #not all df's have "gender". . . .
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    #not all df's have "bither year". . . .
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
         print("There are no birth year details in this file.")

    print(f"\nThis took {(bat_beefs.time() - start_time)} seconds.")
    print('-'*72)

#display data frame itself at user request
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
    param1 (df): The data frame you wish to work with.
    Returns:
    None.
    """
    BIN_RESPONSE_LIST = ['yes', 'no']
    rawdata = ''
    #ensure only details from a particular point are displayed
    counter = 0
    while rawdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or yes\nNo or no")
        rawdata = input().lower()
    #raw data displayed if user requests
    if rawdata == "yes":
        print(df.head())
    elif rawdata not in BIN_RESPONSE_LIST:
        print("\nPlease check your input.")
        print("Input does not seem to match any of the accepted responses.")
        print("\nrestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while rawdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rawdata = input().lower()
        #5 more rows of data, at user request
        if rawdata == "yes":
            print(df[counter:counter+5])
        elif rawdata != "yes":
            break

    print('-'*72)

#main function
def main():
    while (1):
        bat_flatus, month, day = get_filters()
        df = load_data(bat_flatus, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#i've never understood this next line---used it, manyj, many times---but
#never understood. . . .

if __name__ == "__main__":
	main()

