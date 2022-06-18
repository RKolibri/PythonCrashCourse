try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
    print(risk)
except ValueError:
    print("Please use only numeric values (NUMBERS)")
except ZeroDivisionError:
    print("Age cannot be zero")
