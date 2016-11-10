from datetime import datetime, time, timedelta
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def setAlarm():
    eventList = getEvents()
    timeToGetReady = timedelta(hours=1)
    alarmTime = 0
    latestEvent = datetime.today()
    latestEvent.replace(hour=11,minute=0,second=0)
    if eventList:
        for event in eventList:
            timeOfEvent = datetime.datetime.strptime(event[0],"%Y-%M-%dT%H:%M:%S") #this line doesn't quite parse right yet

            if timeOfEvent < datetime.now():
                continue
            if timeOfEvent > latestEvent:
                alarmTime = latestEvent - timeToGetReady
                break
            alarmTime = timeOfEvent - timeToGetReady
    else:
        alarmTime = latestEvent - timeToGetReady
    #set alarm to go off at alarmTime
t = Timer(secs, setAlarm)
t.start()
