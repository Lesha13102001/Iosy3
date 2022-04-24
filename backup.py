import time
from datetime import date,datetime

d = datetime.today()

b="2020-05-13"
l=datetime.strptime(b, "%Y-%m-%d")

r=datetime.strptime("2010-05-13", "%Y-%m-%d")

r=l-d


q=r.days

print(q)
if q < 1:
    print("yess")


