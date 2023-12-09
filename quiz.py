print("Welcome to the quiz.")

playing = input("Do you want to play? ")

if playing != "y":
    quit()
print("Okay, let's play!")

score = 0

answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("You got it right!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ML stand for? ")
if answer.lower() == "machine learning":
    print("You got it right!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does AI stand for? ")
if answer.lower() == "artificial intelligence":
    print("You got it right!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does COA stand for? ")
if answer.lower() == "computer organization and architecture":
    print("You got it right!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does OOP stand for? ")
if answer.lower() == "object oriented programming":
    print("You got it right!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%")

