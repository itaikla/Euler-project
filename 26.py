from decimal import *
import re

maxlen = 0
getcontext().prec = 30

for d in range(1, 1000):
    pattern = re.search(r"^[0-9]\.[0-9]*([0-9]{2,}?)(\1+)[0-9]*?$", str(Decimal(1)/Decimal(d)))
    if pattern is not None:
        length = len(pattern.group(1))
    else:
        length = 0

    if length > maxlen:
        maxlen = length
        result = d

print result
print maxlen
