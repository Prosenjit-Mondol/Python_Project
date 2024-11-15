import random
au=random.randint(1,100)

guess=int(input("Gaess a number  "))
count=1
while guess!=au:
    if guess<au:
        print("Guess higher")
    else:
        print("Guess lower")

    guess=int(input("Guess a number  "))
    count+=1

print("Correct Guess")
print("You took ",count," attemps")