def new():
    name=input("Enter name")
    last=input("Enter last name:")
    grade=float(input("Enter grade: "))
    return name, last, grade
print(new())