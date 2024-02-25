#datetime
#ex1
import datetime
today=datetime.datetime.now()
datetime.timedelta(days=5)
print(today-datetime.timedelta(days=5))

#ex2
import datetime
today=datetime.datetime.now().strftime("%A")
(datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%A")
print((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%A"))
print(today)
print((datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%A"))

#ex3
import datetime
today = datetime.datetime.now().replace(microsecond=0)
print(today)

#ex4
import datetime
time1=datetime.datetime.now()
time2=datetime.datetime.now() - datetime.timedelta(hours=1)
print((time1 - time2).total_seconds())
