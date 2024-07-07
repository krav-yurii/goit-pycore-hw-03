import datetime

def get_upcoming_birthdays(users):
    """
    Determines which colleagues have birthdays in the next 7 days, including today.
    
    Parameters:
    users (list): A list of dictionaries, each containing keys 'name' (user's name, str) 
                  and 'birthday' (user's birthday, str in the format 'YYYY.MM.DD').
    
    Returns:
    list: A list of dictionaries, each containing 'name' (user's name, str) and 
          'congratulation_date' (date of congratulations, str in the format 'YYYY.MM.DD').
    """

    today = datetime.date.today()
    upcoming_birthdays = []

    for user in users:
        name = user["name"]
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        

        birthday_this_year = birthday.replace(year=today.year)
        

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        

        days_until_birthday = (birthday_this_year - today).days
        

        if 0 <= days_until_birthday <= 7:
      
            if birthday_this_year.weekday() >= 5:  
                days_to_next_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + datetime.timedelta(days=days_to_next_monday)
            else:
                congratulation_date = birthday_this_year
            
    
            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Example usage
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith", "birthday": "1990.07.09"}

]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of greetings for this week:", upcoming_birthdays)

