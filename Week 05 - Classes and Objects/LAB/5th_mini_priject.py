"""
RECORD CHECK  -  my version
===========================

Name  :  Vida Hariz
Lane  :  Cybersecurity
Date  :  October 29th 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    def __init__(self, label, value, limit):
        """save the label, value and limit of the record"""
        self.label=label
        self.value=value 
        self.limit=limit 
    def status(self):
        """Return OVER LIMIT, WARNING or OK based on percent."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

with open ("My_records.txt", "w") as f:
    f.write("srv-01,80.0,100.0\n")
    f.write("srv-02,95.0,100.0\n")
    f.write("srv-03,120.0,100.0")
def load_records(path):
    """Reads label,value,limit lines from a file and returns a list of Record """
    records =[]
    with open (path) as f:
        for line in f:
            label, value, limit= line.strip() .split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

records=load_records("My_records.txt")
over_count=0
for record in records:
    if record.status()== "OVER LIMIT":
        over_count+=1
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"value: {record.value}")
    print(f"limit: {record.limit}")
    print(f"status: {record.status()}")
    print("=" * 34)
print ()
print(f" Total over limit: {over_count}")
