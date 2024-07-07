from datetime import datetime

def get_days_from_today(date):

    target_date = datetime.strptime(date, '%Y-%m-%d')
    
    today_date = datetime.now()

    difference = today_date - target_date

    return difference.days


print(get_days_from_today('2024-07-06')) 