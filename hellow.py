score = 0

print("Welcome to the Quiz!")

# Q1
print("\n1. What is the capital of usa?")
print("a) la \nb)washington dc\nc) new york")
ans = input("Your answer: ")
if ans.lower() == "b":
    score += 1

# Q2
print("\n2. Which is the largest planet?")
print("a) Earth\nb) Mars\nc) Jupiter")
ans = input("Your answer: ")
if ans.lower() == "c":
    score += 1

# Q3
print("\n3. Who invented the computer?")
print("a) Charles Babbage\nb) Newton\nc) Einstein")
ans = input("Your answer: ")
if ans.lower() == "a":
    score += 1

print("\nYour total score is:", score, "/ 3")


