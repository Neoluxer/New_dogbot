from datetime import timedelta, datetime


delta = timedelta(days=3220)
today = datetime.now()
date=today-delta
print(date)