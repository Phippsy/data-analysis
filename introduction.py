val = "español"
val_utf8 = val.encode('utf-8')
print(val_utf8)
print(type(val_utf8))

## Date-time
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
print(dt.day)
print(dt.minute)
print(dt.date())
print(dt.time())
print("replacing datetime fields: {}".format(dt.replace(minute=0, second=0)))

print("Timedeltas: {}".format(datetime(2020, 10, 29, 10, 30, 21) - dt))

## Control flow

### For loops
sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value

print(total)

# ternary operators
boogle = "4 is more than 5" if 4 > 5 else "4 is not more than 5"
print(boogle)

bagel = "4 is more than 3" if 4 > 3 else "4 is not more than 3"
print(bagel)
