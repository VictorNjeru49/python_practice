import random

for item in ['python', 'java', 'express']:
    print(item)

#range(1, 5), range(5,6,10)

for i in range(1, 5):
    print(i)

for i in range(5, 6, 10):
    print(i)

price =[10, 20, 60]
total= 0

for i in price:
    total += i

for i in range(5):
    print(random.random())
    print(random.randint(1, 10))

members= ['victor', 'admin', 'kevin', 'joe']
leader = random.choice(members)

print(leader)