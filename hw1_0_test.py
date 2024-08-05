import hw1_0


def test_sum():
    assert hw1_0.sum(1,2) == 3, 'Failed when a = 1 and b = 2'
    assert hw1_0.sum(2,-3) == -1, 'Failed when a = 2 and b = -3'
    assert hw1_0.sum(3,-4.5) == -1.5, 'Failed when a = 3 and b = -4.5'
    print("All tests passed")

def main():
    test_sum()

if __name__ == "__main__":
    main()