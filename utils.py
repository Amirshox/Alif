from datetime import datetime


def date_validator(start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, "%d-%m-%Y/%H:%M")
        end_date = datetime.strptime(end_date, "%d-%m-%Y/%H:%M")
        if end_date > start_date >= datetime.now():
            return start_date, end_date
        else:
            return False, False
    except ValueError:
        return False, False
