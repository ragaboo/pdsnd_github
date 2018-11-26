import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    while True:
        city = input("Which city\'s bikeshare data would you like to analyze? (Chicago, New York City, or Washington) ").lower()
        if city.lower() in CITY_DATA.keys():
            break
        print("{} doesn\'t appear to be a city we have data on. Please try again.".format(city, city))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = None
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input("Which month\'s bikeshare data would you like to analyze? (January through June only. Type \"all\" if you don't want to filter by month) ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input("Which day of week\'s bikeshare data would you like to analyze? (Type \"Monday\", \"Tuesday\", etc. Type \"all\" if you don't want to filter by day of week) ").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month of to rent bikes is {}. \n".format(popular_month))

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("The most popular day of week of to rent bikes is {}. \n".format(popular_day_of_week))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour of to rent bikes is {}. \n".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular starting station is {}. \n".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most popular ending station is {}. \n".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combo Station'] = df['Start Station'] + ' --> ' + df['End Station']
    combo_station = df['Combo Station'].mode()[0]
    print("The most popular travel route is {}. \n".format(combo_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The combined total duration of all trips that match your filters was {} minutes. \n".format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The average trip duration was {} minutes. \n".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts for the different types of users are:")
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print("\n The counts for the different genders are:")
        print(genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()
        print("\n The earliest birth year is:", int(early_birth))
        print("The most recent birth year is:", int(recent_birth))
        print("The most common birth year is:", int(common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    show_raw = None
    start = 0
    end = 5
    while True:
        show_raw = input("Would you like to see the full dataset (in 5-row increments)? Type \"yes\" or \"no\". ").lower()
        if show_raw.lower() in ['yes', 'no']:
            break
        print("We didn't understand. Try again? \n")
    while show_raw == 'yes':
        print(df[df.columns[0:-1]].iloc[start:end])
        start += 5
        end += 5
        more_rows = input('\nWould you like to see 5 more rows? Enter \"yes\" or \"no\".\n')
        if more_rows.lower() != 'yes':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to start this program over? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
