import random

tr = True

print("If you want to complete the randomizer, write stop")

print("Enter range from: ")

while tr == True:
    diap1 = input()
    if diap1.isdigit():
        diap1 = int(diap1)
        print("Enter range to: ")

        diap2 = int(input())

        print("result: ", random.randint(diap1,diap2))
        
        print("Enter range from: ")
    elif diap1 == "stop":
        break
    else:
        print("error!")
        break