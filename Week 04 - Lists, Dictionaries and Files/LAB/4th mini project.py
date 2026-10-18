"""
RECORD CHECK  -  my version
===========================

Name  : Vida Hariz
Lane  :   Cybersecurity
Date  : October 18th 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of (percent):
    """Returns OVER LIMIT, WARNING or OK for the percent"""
    if percent>= 100:
        return "OVER LIMIT"
    elif percent>= 90:
        return "WARNING"
    else:
        return "OK"
    
def check_record(value, limit):
    """Returns difference, percent and status for a report"""
    difference = value - limit
    percent = (value/limit)*100
    status= status_of(percent)
    return difference, percent, status
difference, percent, status = check_record(87.0, 100.0)


def print_report(label, value, limit, difference, percent, status):
    """It prints all of the report"""
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


with open ("Mini_project.txt","w") as f:
    f.write("svr-01, 90, 100\n")
    f.write("svr-02, 50, 120\n")
    f.write("svr-03, 75, 90\n")

def load_records(path) :
    """Reads label,value,limit lines from a file and returns the list """
    records =[]
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append ({"label":label, "value": float(value), "limit": float(limit)})
        return records
try:
    records = (load_records("Mini_project.txt"))
except FileNotFoundError :
    print("Mini_project.txt not found")
    records=[]

for record in records:
    difference, percent, status= check_record(record["value"], record["limit"])
    print_report(record["label"],record["value"],record["limit"],difference,percent,status)


