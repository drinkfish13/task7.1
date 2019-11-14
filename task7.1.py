from datetime import datetime
from datetime import timedelta

def date_range(): # Напишите функцию date_range, которая возвращает список дней между датами start_date и end_date. Даты должны вводиться в формате YYYY-MM-DD.-
    list_date =[]
    start_date = input()
    end_date = input()
    start_date_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    end_date_datetime -= timedelta(days=1)
    while start_date_datetime < end_date_datetime:
        start_date_datetime += timedelta(days=1)
        list_date.append(datetime.strftime(start_date_datetime, '%Y-%m-%d'))
    return list_date
print(date_range())