'''Additional task
– to show the closest leap year
 in case if entered year is not leap'''


def is_year_leap(year):
    return not bool(year % 4)


year = input('Please input year - ')

try:
    y = int(year)
    while y:
        if is_year_leap(y):
            print('Clasest leap year is {}'.format(y))
            break
        y += 1
except:
    print('You input non-numeric symbols')
