"""
RECORD CHECK  -  my version
===========================

Name  : Vida Hariz
Lane  :   Cyber      (delete two)
Date  : 30th September 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



label = input("Enter label: ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))




difference = first - second   
percent = (first / second) * 100      




print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"First number  : {first:>10.2f}")
print(f"Second number : {second:>10.2f}")
print(f"Difference    : {difference:>10.2f}")
print(f"Percentage    : {percent:>10.2f} %")

print("=" * 34)



