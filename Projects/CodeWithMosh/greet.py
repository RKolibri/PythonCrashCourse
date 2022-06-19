def greet_user(firstname, lastname, age, email):
    print(f"Hi {firstname.title()} {lastname.title()}",
          f"you are {age}", "years old!",
          f"Your email is: {email}")
    print("Welcome aboard")


def calc_cost(price, shipping, discount):
    totalcost = price + shipping * discount
    print("Total Cost is: ", totalcost, "$")


greet_user("Klevis", "Resulaj", 26, "klevis@resulaj.eu")

calc_cost(price=50, shipping=5, discount=0.5)
calc_cost(150, 15, 0.15)
