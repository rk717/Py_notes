我们写程序对时间的处理可以归为以下三种： 
时间的显示：在屏幕显示，记录日志等。
时间的转换：比如把字符串格式的日期转化成python中的日期类型。
时间的运算：计算两个日期间的差值等。

import time

print(time.time())     #返回当前时间的时间戳
print(time.localtime()) #将一个时间戳转换为当前时区的struct_time。 若secs参数未提供，则以当前时间为准。
print(time.gmtime())   #和localtime()的方法类似，gmtime()方法时将一个时间戳转换为UTC时区（0时区)的struct_time。

print(time.strftime("%Y-%m-%d %H:%M",time.localtime()))
2020-04-10 16:51

print(time.strptime("2020/04/01 19:30", "%Y/%m/%d %H:%M"))
time.struct_time(tm_year=2020, tm_mon=4, tm_mday=1, tm_hour=19, tm_min=30, tm_sec=0, tm_wday=2, tm_yday=92, tm_isdst=-1)

%d: Day of the month as a decimal number [01,31].
%B: Local full months name.
%H: 24 hr
...

-----------------------------------------------
import datetime

print(datetime.datetime.now())
2020-04-10 16:55:48.183270




