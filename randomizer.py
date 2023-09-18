import random

tr = True

print("If you want to complete the randomizer, write stop")

print("Enter range from: ")

while tr == True:
    rng1 = input()
    if rng1.isdigit():
        rng1 = int(diap1)
        print("Enter range to: ")

        rng2 = int(input())

        print("result: ", random.randint(rng1,rng2))
        
        print("Enter range from: ")
    elif rng1 == "stop":
        break
    else:
        print("error!")
        break
