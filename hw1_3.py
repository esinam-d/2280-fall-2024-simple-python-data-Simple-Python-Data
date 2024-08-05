# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday.
# If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights
# you would return home on day 6 (Saturday).
# Write a general version of the program which calculate
# the return day given the leaving day and the holiday length.
# Example: leaving day 3, holiday length 10 -> return day 6
def calculate_return_day(leaving_day, holiday_length):
    pass

if __name__ == '__main__':
    leaving_day = int(input('Enter leaving day: '))
    holiday_length = int(input('Enter holiday length: '))
    return_day = calculate_return_day(leaving_day, holiday_length)
    print(f'Return day: {return_day}')
