# while loop

i = 1
while i<=5:
    print(i)
    i += 1
print("done")


while i<=5:
    print('*' * i)
    i += 1
 
 secret_number = 9
 geuss_count=0
 guess_limit = 3
 while geuss_count < guess_limit:
     guess = int(input("Guess the secret number: "))
     if guess == secret_number:
         print("Congratulations! You guessed the number.")
         break
     else:
         print("Sorry, that's not it. Try again.")
     geuss_count += 1