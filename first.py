from datetime import datetime

def get_days_from_today(date):
    """
    Calculates the number of days between the given date and today.
    
    Parameters:
    date (str): Date in the format 'YYYY-MM-DD'.
    
    Returns:
    int: Number of days from the given date to today.
         Negative if the given date is in the future.
    
    Raises:
    ValueError: If the date is in an incorrect format.
    """

    try:
        target_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Date must be in 'YYYY-MM-DD' format")
    
    today_date = datetime.today()

    difference = today_date - target_date

    return difference.days


try:
    print(get_days_from_today('2021-10-09'))
except ValueError as e:
    print(e)