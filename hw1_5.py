import math
# Prompt the user to enter the number of miles driven and the number of gallons used.
# Write a function that will compute MPG for a car.
# Print a nice message with the answer.
def compute_mpg(miles, gallons):
    # put your code here
    pass

if __name__ == "__main__":
    miles = float(input('Enter miles driven: '))
    gallons = float(input('Enter gallons used: '))
    print(f'The MPG is {compute_mpg(miles, gallons):.5f}')