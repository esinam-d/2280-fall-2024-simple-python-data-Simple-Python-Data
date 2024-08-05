import hw1_5

def test_compute_mpg():
    assert abs(hw1_5.compute_mpg(50, 2) - 25) < 0.0001, 'Failed when miles = 50 and gallons = 2'
    assert abs(hw1_5.compute_mpg(135, 3) - 45) < 0.0001, 'Failed when miles = 135 and gallons = 3'
    assert abs(hw1_5.compute_mpg(200, 5.5) - 36.4) < 1, 'Failed when miles = 200 and gallons = 5.5'
    print('All tests passed')
def main():
    test_compute_mpg()

if __name__ == '__main__':
    main()