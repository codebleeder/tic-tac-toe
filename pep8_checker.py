import pep8
from sys import argv

checker = pep8.Checker(argv[1])
checker.check_all()
