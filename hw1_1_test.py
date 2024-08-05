import hw1_1

def test_compute_area():
    assert hw1_1.compute_area(1) == 3.141592653589793, 'Failed when radius = 1'
    assert hw1_1.compute_area(2) == 12.566370614359172, 'Failed when radius = 2'
    assert hw1_1.compute_area(3) == 28.274333882308138, 'Failed when radius = 3'
    print("All tests passed")

def main():
    test_compute_area()

if __name__ == "__main__":
    main()