import time
import math


def changeTime(allTime):
    day = 24 * 60 * 60
    hour = 60 * 60
    min = 60
    if allTime < 60:
        return "%d 秒" % math.ceil(allTime)
    elif allTime > day:
        days = divmod(allTime, day)
        return "%d 天, %s" % (int(days[0]), changeTime(days[1]))
    elif allTime > hour:
        hours = divmod(allTime, hour)
        return '%d 小时, %s' % (int(hours[0]), changeTime(hours[1]))
    else:
        mins = divmod(allTime, min)
        return "%d 分, %d 秒" % (int(mins[0]), math.ceil(mins[1]))


nums = 9790
t = time.time()
data = changeTime(nums)
print (time.time() -t)
print (data)

b = 5
def a():
    b = 1;
    def vv():
        c = 2 +b
        return c
    return vv,b
x,y=a()
print(x())
print(y)
print(b)
