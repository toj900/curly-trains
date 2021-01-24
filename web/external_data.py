import sys
import datetime

time = datetime.datetime.now()
output = "Hi %s current time is %s" % (sys.argv[1], time)
output = f"Hi {sys.argv[1]} the current time is is {time}"
print(output)