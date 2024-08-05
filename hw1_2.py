# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours (lapse time), it will go off at 15.
# Write a Python program to calculate the go off time given the current time and the lapse time.
# Example current time 13, lapse time 50 -> go off time 15
def compute_alarm_time(current_time, lapse_time):
    # put your code here
    pass

if __name__ == "__main__":
    current_time = int(input('Enter current time: '))
    lapse_time = int(input('Enter lapse time: '))
    print(f'The alarm will go off at: {compute_alarm_time(current_time, lapse_time)}')