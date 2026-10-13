"""
RECORD CHECK  -  my version
===========================

Name  :  Vida Hariz
Lane  :  Cybersecurity
Date  :  11th October

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Return OVER LIMIT, WARNING, OK for the percent"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
def check(value, limit):
    """Returns the difference and the percentage as two values"""
    difference = value-limit  
    percent = value/limit * 100    
    return difference, percent
def print_report(label, value, limit, difference, percent, status):
    """It prints all or the report"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"    Used      :{value:10.2f}")
    print(f"    Total     :{limit:10.2f}")
    print(f"    Free      :{-difference:10.2f}")
    print(f"    Percent   :{percent:10.2f}%")
    print(f"    Status    :{status:>10}")
    print("=" * 34)


while True:
    label = input ("Enter a label(or quit): ")  
    if label== "quit":
        break    
    value = float(input("Enter the used: "))     
    limit = float(input("Enter the total: "))     
    
    difference, percent=check(value, limit)
    status = status_of(percent)         
    
    print_report(label, value, limit, difference, percent, status)
