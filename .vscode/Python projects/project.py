print("Hey buddy, what's going on!")
answer = input().lower()

if answer == "nothing":
    print("Then let's play a game and check your knowledge:")
else:
    print("Type correctly, I know you want to play ")

answer = input().lower()

if answer == "ok then":
    print("\nOK! Be ready for the quiz buddy! \n")

    questions = [
        ("What does CPU stand for? ", "central processing unit"),
        ("What does NIC stand for? ", "network interface card"),
        ("What does Lexical Analyzer do? ", "analyzes the source code for tokens"),
        ("What does CU mean? ", "control unit"),
        ("What does OS do? ", "manages hardware and software resources")
    ]

    score = 0

    #  Loop through questions
    for q, ans in questions:
        user_answer = input(q + "\n").lower()

        if user_answer == ans:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer: {ans}\n")

    print("Your final score is:", score, "/", len(questions))

    # 🏆 Performance
    if score <= 2:
        print(" Poor performance")
    elif score <= 4:
        print(" Good job")
    else:
        print(" Wonderful performance")

else:
    print("Type correctly, I know you want to play 😄")