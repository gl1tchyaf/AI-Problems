print("Enter your mark: ")
mark = int(input())
if mark<60:
    print("Your grade is F")
    print("Your grade point is 0.00")
elif (mark >=60 and mark <63):
    print("Your grade is D")
    print("Your grade point is 1.00")
elif (mark >=63 and mark <67):
    print("Your grade is D+")
    print("Your grade point is 1.30")
elif (mark >=67 and mark <70):
    print("Your grade is C-")
    print("Your grade point is 1.70")
elif (mark >=70 and mark <73):
    print("Your grade is C")
    print("Your grade point is 2.00")
elif (mark >=73 and mark <77):
    print("Your grade is C+")
    print("Your grade point is 2.30")
elif (mark >=77 and mark <80):
    print("Your grade is B-")
    print("Your grade point is 2.70")
elif (mark >=80 and mark <83):
    print("Your grade is B")
    print("Your grade point is 3.00")
elif (mark >=83 and mark <87):
    print("Your grade is B+")
    print("Your grade point is 3.30")
elif (mark >=87 and mark <90):
    print("Your grade is A-")
    print("Your grade point is 3.70")
elif (mark >=90 and mark <97):
    print("Your grade is A")
    print("Your grade point is 4.00")
elif (mark >=97 and mark <=100):
    print("Your grade is A+")
    print("Your grade point is 4.00")
else:
    print("Invalid input")