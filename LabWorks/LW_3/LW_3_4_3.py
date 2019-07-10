'''Optional task
- Add a possibility to print
all the leap years within given range'''


def is_year_leap(year):
    return not bool(year % 4)


try:
    y1, y2 = (int(input('Enter year - ')) for _ in range(2))

    if y2 <= y1:
        print('Uncorrected values of years!')
    else:
        for y in range(y1, y2):
            if is_year_leap(y):
                print(y)
except:
    print('You input non-numeric symbols')
