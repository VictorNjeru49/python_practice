
number = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

# append(50)
# insert(3, 40)
# remove(7)
# clear()
# pop()
# number.index (5)
# 50 in number  to check for if exists
# sort()
# reverse()

# [] for array elements () tuples no change

numbers = [1, 2, 3, 4, 5, 6, 7]

for i in numbers:
    if i in not in uniques:
        uniques.append(i)
        print(uniques)

coordinates = (1, 2, 3, 4, 5, 6, 7)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
x,y,z = coordinates


customer = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}
print (customer["name"])
print (customer["address.street"])
print (customer.get("zip, 646"))

phone = input("phone: ")
digital_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ""

for digit in phone:
     output += digital_mapping.get(digit, "Invalid digit") + " "

     print(output)