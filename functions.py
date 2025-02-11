def greet_user():
    """Display a personalized greeting to the user."""
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

print("start")
greet_user()
print("end")

def greet_people(name): # greet_people(first_name, last_name)
    print(f'Hi {name}!')
    print('welcome aboard')

greet_people('John Doe') # greet_people(last_name = 'John Doe', first_name = 'mary smith')

# calc_costs(total_cost = 50, shipping = 5, rate = 0.1)


def square(number):
    return number * number

print(square(5)) # 25

def lbs_to_kg(weight):
    return weight * 0.453592

def kg_to_lbs(weight):
    return weight / 0.453592