from datetime import datetime


def days_since_birthday(birthday_str):
    # Convert the birthday string to a datetime object
    birthday = datetime.strptime(birthday_str, "%d-%m-%Y")

    # Get today's date
    today = datetime.now()

    # Calculate the difference in days
    days_passed = (today - birthday).days

    return days_passed


# Example usage
birthday = "20-11-2002"
print(days_since_birthday(birthday))

