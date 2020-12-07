from sys import argv

try:
    salary = float(argv[1]) * float(argv[2]) + float(argv[3])
    print('Your salary is: ', salary)
except (ValueError, IndexError):
    print('Three numbers need')
