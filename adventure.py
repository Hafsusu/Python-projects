name = input("Type your name: ")
print("Welcome", name, "To this adventure.")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. which way you wanna go? ").lower()
if answer == "left":
    answer = input("You come to a river, you can swim across or walk around. you type walk or swim: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Invalid choice!")
elif answer == "right":
    answer == input("You come to a bridge, it looks wobbly, do you want to cross it or turn back? ").lower()
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge to meet  a stranger, do you talk to the them? ").lower()
        if answer == "yes":
            print("You talk to the stranger,  you won a treasure!")
        elif answer == "no":
            print("You offended the stranger, you lost!")
        else:
            print("Invalid choice!")
else:
    print("Invalid choice!")
print("Thank you for trying the adventure.")
