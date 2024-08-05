import hw1_6

def test_compute_fahrenheit():
    assert abs(hw1_6.compute_fahrenheit(35) - 95) < 0.0001, 'Failed when Celcius degree = 35'
    assert abs(hw1_6.compute_fahrenheit(-10) - 14) < 0.0001, 'Failed when Celcius degree = -10'
    assert abs(hw1_6.compute_fahrenheit(100) - 212) < 0.0001, 'Failed when Celcius degree = 100'
    assert abs(hw1_6.compute_fahrenheit(0) - 32) < 0.0001, 'Failed when Celcius degree = 0'
    print('All tests passed')
def main():
    test_compute_fahrenheit()

if __name__ == '__main__':
    main()