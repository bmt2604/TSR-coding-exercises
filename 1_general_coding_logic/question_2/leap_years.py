def leap_year(year):
    """Returns True if year is a leap year.
    Otherwise, False."""

    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return False


def next_leap_years(year, n):
    """Prints next n leap years starting at given year."""

    count = 0

    while count != n:
        if leap_year(year):
            print(year)
            count += 1
        year += 1


next_leap_years(2021, 20)  # next 20 leap years
