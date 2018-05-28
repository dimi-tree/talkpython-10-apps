from datetime import date


def print_the_header():
    app_header = 'BIRTHDAY APP'
    print('-' * (20 + len(app_header)))
    print(' ' * 10 + app_header)
    print('-' * (20 + len(app_header)))
    print()


def get_birthday_from_user():
    print('When were you born?')
    year = int(input('Year [YYYY]: ').strip())
    month = int(input('Month [MM]: ').strip())
    day = int(input('Day [DD]: ').strip())
    return date(year, month, day)


def compute_days_between_dates(original_date, target_date):
    this_year = date(year=target_date.year, month=original_date.month, day=original_date.day)
    return (this_year - target_date).days


def print_birthday_information(days):
    if days < 0:
        print(f'You had your birthday {days} ago this year.')
    elif days > 0:
        print(f'Your birthday is in {days} days!')
    else:
        print('Today is your birthday!!!')


def main():
    print_the_header()
    bday = get_birthday_from_user()
    number_of_days = compute_days_between_dates(bday, date.today())
    print_birthday_information(number_of_days)


if __name__ == '__main__':
    main()
