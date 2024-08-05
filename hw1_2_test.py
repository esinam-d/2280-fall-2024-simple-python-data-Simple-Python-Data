import hw1_2

def test_compute_alarm_time():
    assert hw1_2.compute_alarm_time(1, 7) == 8, 'Failed when current time = 1 and lapse time = 7'
    assert hw1_2.compute_alarm_time(3, 22) == 1, 'Failed when current time = 3 and lapse time = 22'
    assert hw1_2.compute_alarm_time(13, 50) == 15, 'Failed when current time = 13 and lapse time = 50'
    print("All tests passed")

def main():
    test_compute_alarm_time()

if __name__ == "__main__":
    main()