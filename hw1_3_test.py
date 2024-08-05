import hw1_3

def test_calculate_return_day():
    assert hw1_3.calculate_return_day(3, 1) == 4, 'Failed when leaving day = 3 and holiday length = 1'
    assert hw1_3.calculate_return_day(3, 10) == 6, 'Failed when leaving day = 3 and holiday length = 10'
    assert hw1_3.calculate_return_day(3, 20) == 2, 'Failed when leaving day = 3 and holiday length = 20'
    print("All tests passed")

def main():
    test_calculate_return_day()

if __name__ == "__main__":
    main()