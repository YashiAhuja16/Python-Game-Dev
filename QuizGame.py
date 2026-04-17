quiz = (("What is 2 + 2?", "4"), ("What is the capital of California?", "Sacramento"), ("What color is the sky?", "Blue"))

score = 0

for x, a in quiz:
    print(x)
    answer = input("Answer: ")
    
    if answer.lower() == a.lower():
        print("Correct")
        score = score + 1
    else:
        print("Wrong, correct answer is", a)

print("Your score is:", score)