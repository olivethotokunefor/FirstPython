grade1 = input("Enter your mathematics score: ")
grade2 = input("Enter your English score: ")
grade3 = input("Enter yout History score: ")
grade4 = input("Enter you Chemistry score: ")

average = int(grade1) + int(grade2) + int(grade3) +int(grade4) // 4

if int(grade1) > 100 or int(grade2) > 100 or int(grade3) > 100 or int(grade4) > 100:
    print("Score too high")
elif int(grade1) < 0 or int(grade2) < 0 or int(grade3) < 0 or int(grade4) < 0:
    print("Score is too low")
else :
    if average >= 70:
        print("A")
    elif average >= 50 and average < 70:
        print("B")
    elif average < 50 and average >= 30:
        print("C")
    else:
        print("D")
