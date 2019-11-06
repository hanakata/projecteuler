def main(startYear, endYear):
    beginningOfMonth = 1
    result = 0
    for i in range(startYear, endYear):
        leapYear = leapYearJudge(i)
        for j in range(1, 13):
            days = monthDay(j, leapYear)
            beginningOfMonth = dayOfTheWeek(days, beginningOfMonth)
            if beginningOfMonth == 7:
                result += 1
    return result


def leapYearJudge(year):
    leapYear = 0
    if year % 4 == 0:
        if year % 400 != 0 and year % 100 == 0:
            pass
        else:
            leapYear = 1
    return leapYear


def monthDay(month, leapYear):
    checkMonth = [1, 3, 5, 7, 8, 10, 12]
    days = 0
    if month == 2 and leapYear == 1:
        days = 29
    elif month == 2:
        days = 28
    elif month in checkMonth:
        days = 31
    else:
        days = 30
    return days


def dayOfTheWeek(days, beginningOfMonth):
    remainder = days % 7
    beginningOfMonth = beginningOfMonth + remainder
    if beginningOfMonth > 7:
        beginningOfMonth = beginningOfMonth - 7
    return beginningOfMonth


if __name__ == "__main__":
    full = main(1900, 2001)
    minus = main(1900, 1901)
    print(full - minus)
