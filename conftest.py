def pytest_addoption(parser):
    parser.addoption("--a", action="store", default=1, help="Value of a.")
    parser.addoption("--b", action="store", default=2, help="Value of b.")
    parser.addoption("--sum", action="store", default=3, help="Value of sum.")