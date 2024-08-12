year = int(input("Please enter the year: "))
month = int(input("Please enter the month (1-12) that you wish to know the days for: "))

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

def print_month_days(month):
    if 1 <= month <= 12:
        print(f"The number of days in month {month} is: {month_days[month - 1]}")
    else:
        print("Invalid month input. Please enter a number between 1 and 12.")

leap_year(year)
print_month_days(month)
