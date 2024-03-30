from datetime import datetime, timedelta


def generate_dates(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date.date()
        current_date += timedelta(days=1)


start_date = datetime(2024, 3, 1)
end_date = datetime(2025, 3, 10)

for date in generate_dates(start_date, end_date):
    print(date)

#Вирішив погуглити готові модулі, пітон це класно!)