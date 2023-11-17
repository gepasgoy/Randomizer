import random

print("If you want to complete the randomizer, write stop")

print("Enter range from: ")

while True:
    rng1 = input()
    if rng1.isdigit():
        print("Enter range to: ")
        while True:
            try:
                rng2 = int(input())

                print("result: ", random.randint(int(rng1), rng2))

                break
            except ValueError:
                print("Error!Enter a number!")

        print("Enter range from: ")
    elif rng1 == "stop":
        break
    else:
        print("error!")
        break