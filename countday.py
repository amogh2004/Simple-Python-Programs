year1 = int(input("Enter the year as digit: "))
month1 = int(input("Enter the month as digit: "))
date1 = int(input("Enter the date as digit: "))

if month1 > 12:
    print("Wrong month entered")
    exit()


def calculate_days(date, month):
    current_month = 1
    totaldays = 0
    while month != current_month:
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or
                month == 10 or month == 12):
            totaldays += 31
            current_month += 1
        elif month == 4 or month == 6 or month == 9 or month == 11 :
            totaldays += 30
            current_month += 1
        else:
            totaldays += 28
            current_month += 1
    totaldays += date
    return totaldays


if year1 % 4 == 0 and year1 % 100 !=0 or year1 % 400 == 0:
    print("Entered year is a leap year")
    days = calculate_days(date1, month1)
    print("Number of days elapsed this year=")
    print(days+1)

else:
    print("Entered year is not a leap year")
    days = calculate_days(date1, month1)
    print("Number of days elapsed this year=")
    print(days)

exit()
