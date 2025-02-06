try:
age = int(input("age: "))
income : 2000
risk = income/ age
print (age)
except ZeroDivisionError:
    print("Age Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")