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

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input ("Enter a label:")      # replace with an input() call
value = float(input ("Enter a value"))  # replace with an input() call, converted with float()
limit = float(input ("Enter a limit"))    # replace with an input() call, converted with float()


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = value-limit  # replace with your calculation
percent = value/limit * 100      # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

status = ""   # replace with your if / else (or if / elif / else)
if percent >= 100:
    status="OVER LIMIT"
elif percent >= 90:
    status="WARNING"
else:
    status="OK"
print(status)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.


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

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
