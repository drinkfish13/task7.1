from datetime import datetime
from datetime import timedelta

def date_range(): # Напишите функцию date_range, которая возвращает список дней между датами start_date и end_date. Даты должны вводиться в формате YYYY-MM-DD.-
    list_date =[]
    start_date = input()
    end_date = input()
    try: # Проверка на корректность дат. В случае неверного формата должен возвращаться пустой список.
        start_date_datetime = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return list_date
    if start_date_datetime >= end_date_datetime: # Проверка на корректность дат. В случае если start_date > end_date должен возвращаться пустой список.
        return list_date
    end_date_datetime -= timedelta(days=1)
    while start_date_datetime < end_date_datetime:
        start_date_datetime += timedelta(days=1)
        list_date.append(datetime.strftime(start_date_datetime, '%Y-%m-%d'))
    return list_date
print(date_range())
