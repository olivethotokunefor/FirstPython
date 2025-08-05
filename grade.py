def grade_score(score):
    if score > 100:
        print("Score too high")
    elif score < 0:
        print("Score too low")
    else:
        if score >= 70:
            print("Grade: A")
        elif score >= 60:
            print("Grade: B")
        elif score >= 50:
            print("Grade: C")
        elif score >= 40:
            print("Grade: D")
        else:
            print("Grade: F")

user_score = int(input("Enter your score: "))
grade_score(user_score)
