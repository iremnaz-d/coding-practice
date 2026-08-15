#https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    no = calendar.weekday(year, month, day)
    print(calendar.day_name[no].upper())
