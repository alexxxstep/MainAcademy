''' Write a program, which takes a year as input
and returns message if this is a leap year or note.
 Please handle the exceptions which may arise is a user will
  enter non-numeric symbols.'''


def is_year_leap(year):
    '''Return is year leap or not'''
    return not bool(year % 4)

year = input('Please input year - ')

try:
    y = int(year)
    if is_year_leap(y):
        print('Your year {} is a leap!'.format(year))
    else:
        print('Your year {} is not leap!'.format(year))
except:
    print('You input non-numeric symbols')
