import re

def normalize_phone(phone_number):
    """
    Normalizes a phone number to a standard format.

    Parameters:
    phone_number (str): A string containing a phone number in various formats.

    Returns:
    str: The normalized phone number as a string.

    Raises:
    ValueError: If the phone number does not contain any digits.
    """
    
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    print(cleaned_number)

    if not re.search(r'\d', cleaned_number):
        raise ValueError("The phone number must contain at least one digit")

    if cleaned_number.startswith('+'):
        if not cleaned_number.startswith('+380'):
            return cleaned_number
    else:
        if cleaned_number.startswith('380'):
            return '+' + cleaned_number
        else:
            return '+38' + cleaned_number

    return cleaned_number

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "invalid_number"
]

sanitized_numbers = []
for num in raw_numbers:
    try:
        sanitized_number = normalize_phone(num)
        sanitized_numbers.append(sanitized_number)
    except ValueError as e:
        print(f"Error processing number '{num}': {e}")

print("Normalized phone numbers for SMS distribution:", sanitized_numbers)