import datetime


def print_header():
    print('-------------------------')
    print('   Birthday Countdown App')
    print('-------------------------')
    print()


def get_user_birthday():
    print('When is your birthday?')
    bd_year = int(input('In which year were you born? (YYYY): '))
    bd_month = int(input('In which month were you born? (MM): '))
    bd_day = int(input('On what day were you born? (DD): '))
    return datetime.date(year=bd_year, month=bd_month, day=bd_day)


def get_days_between_dates(dt_today, dt_bday):
    thisyear_bday = datetime.date(year=dt_today.year, month=dt_bday.month, day=dt_bday.day)
    days_difference = (thisyear_bday - dt_today).days
    return days_difference


def print_birthday_info(dt_delta):
    if dt_delta > 0:
        print(f'Your birthday is in {dt_delta} days.')
    elif dt_delta < 0:
        print(f'Your birthday was {-dt_delta} days ago.')
    else:
        print('Happy birthday!')


def main():
    print_header()
    bday = get_user_birthday()
    today = datetime.date.today()
    delta = get_days_between_dates(today, bday)
    print_birthday_info(delta)


main()
