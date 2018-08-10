import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july',
    'august', 'september', 'october', 'november', 'december']

DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
    'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Valid cities are; Washington, New York City, and Washington.\n')
    city = input('Please enter name of desired city for inquiry.\n')

    while city.lower() not in CITIES:
        print('Valid cities are; Washington, New York City, and Washington.\n')
        city = input('Please retry and enter a valid city.\n')

    # get user input for month (all, january, february, ... , june)
    month = input('Please enter desired month for inquiry, or type "all" for all months.\n')

    while month.lower() not in MONTHS:
        month = input('Please retry and enter a valid month.\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter desired day for inquiry, or type "all" for all days.\n')

    while day.lower() not in DAYS:
        day = input('Please retry and enter a valid day.\n')

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
    if city == 'new york city':
        city = 'new_york_city'

    # loading csv
    df = pd.read_csv("{}.csv".format(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #creating month, day, hour, trip duration, and trip columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    df['trip'] = df['Start Station'] + ' ' + df['End Station']
    df['duration'] = df['Start Time'] - df['End Time']

    # filtering by month and day
    if month != 'all':
        df = df.query('month == {}'.format(month))

    if day != 'all':
        df = df.query('day == {}'.format(day))

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is;')
    print(df['month'].mode()[0])

    # display the most common day of week
    print('The most common day of week is;')
    print(df['day'].mode()[0])

    # display the most common start hour
    print('The most common start hour is;')
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most commonly used end station is {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('The most commonly used combination of stations is {}'.format(df['trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is {}.'.format(df['duration'].sum()))

    # display mean travel time
    print('Mean travel time is {}.'.format(df['duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types;')
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' not in list(df.columns.values):
        print('Sorry, dataset has no gender data.')
    else:
        print('Counts of gender;')
        print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in list(df.columns.values):
        print('Sorry, dataset has no birth year data.')
    else:
        print('Earliest year of birth: {}'.format(df['Birth Year'].min()))
        print('Most recent year of birth: {}'.format(df['Birth Year'].max()))
        print('Most common year of birth: {}'.format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
