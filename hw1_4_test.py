import hw1_4

def test_compute_sphere_volume():
    assert abs(hw1_4.compute_sphere_volume(5) - 523.5987755982989) < 0.0001, 'Failed when radius = 5'
    assert abs(hw1_4.compute_sphere_volume(7) - 1436.75504) < 0.0001, 'Failed when radius = 7'
    print("All tests passed")

def main():
    test_compute_sphere_volume()

if __name__ == "__main__":
    main()