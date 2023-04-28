def days_in_month(month, year=None):
    """
    Returns the number of days in a month.
    If month is February and year is given, it takes leap year into account.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if year is None:
            return 28
        elif year % 4 != 0:
            return 28
        elif year % 100 != 0:
            return 29
        elif year % 400 != 0:
            return 28
        else:
            return 29

month = int(input("Enter a number between 1 to 12: "))
if month < 1 or month > 12:
    print("Invalid input. Month should be between 1 to 12.")
else:
    if month == 2:
        year = int(input("Enter a year to check if it is a leap year: "))
        days = days_in_month(month, year)
    else:
        days = days_in_month(month)
    if month == 1:
        month_name = "January"
    elif month == 2:
        month_name = "February"
    elif month == 3:
        month_name = "March"
    elif month == 4:
        month_name = "April"
    elif month == 5:
        month_name = "May"
    elif month == 6:
        month_name = "June"
    elif month == 7:
        month_name = "July"
    elif month == 8:
        month_name = "August"
    elif month == 9:
        month_name = "September"
    elif month == 10:
        month_name = "October"
    elif month == 11:
        month_name = "November"
    else:
        month_name = "December"
    print(f"{month_name} has {days} days.")
