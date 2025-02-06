weight = int(input('weight: '))
units = input('(L)bs or (K)g')

if units.upper() == 'L':
    converted weight = weight * 0.45
    print(f'Your weight in kg is {converted_weight}')
else:
    converted_weight = weight / 0.45
    print(f'Your weight in lbs is {converted_weight}')