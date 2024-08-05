#Write a function that output sum of two numbers

def sum(a,b):
    return a+b

if __name__ == "__main__":
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    print(f'The sum is {sum(a,b)}')