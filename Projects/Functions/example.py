from datetime import datetime, date


def greet_user():
    """Display a simple greeting"""
    print("Hello!")
    print("How are you today ?")

    today = date.today()
    # dd/mm/YY
    date_today = today.strftime("%d/%m/%Y")
    print("Today's date is :", date_today)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time is :", current_time)


greet_user()
