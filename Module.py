#Module
import math      #Modules need to be imported.
print(math.sqrt(4))
print(math.log10(100))
print(math.sqrt(60))
print(math.pi)
print(math.sin(math.radians(90)))

# Date module
from datetime import date

print(date.today())

today = date.today()
print(today)

print(today.day, today.month, today.year)

from datetime import datetime
print(datetime.now())
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
