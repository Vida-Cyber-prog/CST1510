"""
RECORD CHECK  -  my version
===========================

Name  : Vida
Lane  : Cybersecurity  
Date  : November 8th 2006

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

df = pd.read_csv("server.csv")
df["percent"]=(df["used"]/df["total"])*100
df["status"]= df["percent"].apply(
    lambda p: "OVER LIMIT" if p>=100 else "WARNING" if p>=90 else "OK")
print(df)


not_ok=df[df["status"]!="OK"]
print(df.groupby("status").size())
df.to_csv("server1.csv", index=False)

import matplotlib.pyplot as plt
df["status"].value_counts().plot(kind="bar")
plt.title("counts per status")
plt.savefig("status_counts.png")
plt.show()
