import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # get user input for city (chicago, new york city, washington). 
    city = input("would you like to see data for chicago, new york, washington?").lower() 
    while city not in ['chicago', 'new york', 'washington']:
        city = input(" invalid input, please enter a city name again: ").lower()
        
    # get user input for month (all, january, february, ... , june) 
    month = input( "which month? january, february, march, april, may, june or all? ").lower()
    while month not in ['january', 'February', 'march', 'april', 'mai','june', 'all']:
        month = input(" invalid input, please enter a month again: ").lower()
                
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("which day? monday, tuesday, wednesday, thursday, friday or all? ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']:
        day = input(" invalid input, please enter a day again: ").lower()
        
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')  
    start_time = time.time()
    
    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    popular_month = df['Start Time'].dt.month.mode()[0]
    
    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]

    # display the most common hour of day
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    
    print("\nMost common month: {}\nMost common day of weeek: {}\nMost common hour of day: {} "
          .format(popular_month, popular_day, popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    commonly_used_station = df['Start Station'].mode()[0]
     
    # display most commonly used end station
    commonly_used_end_station = df['End Station'].mode()[0]
     
    # display most frequent combination of start station and end station trip
    commonly_used_both_station = df[['Start Station','End Station']].mode()
    

    print("\nCommonly used start station: {}\nCommonly used end station: {}\nMost frequent combination of start and end stations:\n{}"
          .format(commonly_used_station,commonly_used_end_station,commonly_used_both_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time 
    total_time_duration = df['Trip Duration'].sum()

    # display mean travel time
    mean_time_duration = df['Trip Duration'].mean()
    

    print("Total time travel  : {}\nAverage travel time: {}\n".format( total_time_duration, mean_time_duration))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if city == 'washington':
        print( "Sorry, no year of birth or gender data to share.")
    else:
        # Display counts of user types
        count_user_types = df['User Type'].value_counts() 
        # Display counts of gender
        count_gender = df['Gender'].value_counts()

        # Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = int(df['Birth Year'].min()) 
        most_recent_year_of_birth = int(df['Birth Year'].max())
        common_year_of_birth = int(df['Birth Year'].mode())
        print("Number of user types:\n{}\nGenders count:\n{} \nEarliest year of birth: {}\nMost recent year of birth: {}\nCommon year of birth: {} "
          .format(count_user_types, count_gender, earliest_year_of_birth, most_recent_year_of_birth, common_year_of_birth))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(pd.read_csv(CITY_DATA[city]))
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)wa

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
