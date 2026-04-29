from datetime import datetime
import pytz
b=pytz.timezone("Asia/kabul")
a=datetime.now(b)
print(a)
for i in pytz.all_timezones:
    print(i)