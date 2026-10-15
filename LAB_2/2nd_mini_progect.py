"""
RECORD CHECK  -  my version
===========================

Name  : Vida Hariz
Lane  :   Cybersecurity
Date  : 3rd of October

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


label = input ("Enter a label:")      # replace with an input() call
value = float(input ("Enter a value"))  # replace with an input() call, converted with float()
limit = float(input ("Enter a limit"))    # replace with an input() call, converted with float()


if percent >= 100:
    status="OVER LIMIT"
elif percent >= 90:
    status="WARNING"
else:
    status="OK"
print(status)



over_count = 0
while True:
    label = input ("Enter a label:")  
    if label == "quit":
        break
    used = float(input ("Enter the used amount: "))  
    total = float(input ("Enter the total: "))
    free= total - used
    percentage = used / total*100
    if percentage >= 100:
        status="OVER LIMIT"
        over_count=over_count+1
    elif percentage >= 90:
        status="WARNING"
    else:
        status="OK"
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print (f"  Used    : {used:>10.2f}")
    print (f"  Total   : {total:>10.2f}")
    print (f"  Free    : {free:>10.2f}")
    print (f"  Percent : {percentage:>10.2f} %")
    print (f"  Status  : {status:>10}")
    print("=" * 34)
print("OVER LIMIT count", over_count)

