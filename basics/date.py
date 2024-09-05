import datetime
    # Get the current time
now = datetime.now()
current_hour = now.hour

# Determine the time of day and print the appropriate greeting
if 5 <= current_hour < 12:
    print("Good morning!")
elif 12 <= current_hour < 17:
    print("Good afternoon!")
elif 17 <= current_hour < 21:
    print("Good evening!")
else:
    print("Good night!")

# Call the function to display the greeting
