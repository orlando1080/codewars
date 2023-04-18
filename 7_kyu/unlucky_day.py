# Description:

# Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

# Find the number of Friday 13th in the given year.

import datetime


def unlucky_days(year):
    count = 0
    for month in range(1, 13):
        date = datetime.date(year, month, 13)
        if date.weekday() == 4:  # 4 represents Friday as per the weekday() method
            count += 1
    return count
