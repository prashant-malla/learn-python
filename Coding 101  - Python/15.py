from datetime import datetime

now = datetime.now()
bday = datetime(now.year, 9, 20)
# print(bday - now)
if bday < now:
    bday=  datetime(now.year + 1, 9, 20)
diff = bday - now
print(diff)