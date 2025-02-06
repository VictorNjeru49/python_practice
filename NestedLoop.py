for x in range( 5):
    for y in range( 4):
        print(f"({x}, {y})")

number = [5,2,5,3,2]

for i in range(len(number)):
    for j in range(i+1, len(number)):
        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]

# *****
# **
# *****
# ***
# **
for x_count in numbers:
    output = ''
    for y_count in range(x_count):
        print(output)

number = [4, 8, 3, 20, 46, 66]
max = number[0]

for i  in number:
    if number > max:
        max = number
        print(max)