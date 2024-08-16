import hw1_0
import pytest


@pytest.fixture
def a_b_sum(request):
    a = float(request.config.getoption('--a'))
    b = float(request.config.getoption('--b'))
    sum = float(request.config.getoption('--sum'))
    print(a, b, sum)
    return a, b, sum




def test_sum(a_b_sum):
    a, b, sum = a_b_sum
    assert hw1_0.sum(1,2) == 3, 'Failed when a = 1 and b = 2'
    assert hw1_0.sum(2,-3) == -1, 'Failed when a = 2 and b = -3'
    assert hw1_0.sum(3,-4.5) == -1.5, 'Failed when a = 3 and b = -4.5'
    assert hw1_0.sum(a,b) == sum, 'Failed teacher test'
    print("All tests passed")

def main():
    test_sum()

if __name__ == "__main__":
    main()