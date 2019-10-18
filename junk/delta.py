import datetime
import time
import json
import re

format_path= re.compile( 
    r"^\S+\s-\s" 
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]" 
)

threshold = time.strptime('00:01:00,000'.split(',')[0],'%H:%M:%S')
tick = datetime.timedelta(hours=threshold.tm_hour,minutes=threshold.tm_min,seconds=threshold.tm_sec).total_seconds()
zero_time = datetime.timedelta(hours=0,minutes=0,seconds=0)
zero_tick = zero_time.total_seconds()
format_date = '%d/%b/%Y:%H:%M:%S'

obj = {}
test = open('very/big/log','r')

for line in test:
  try:
      chunk = line.split('+', 1)[0].split('-', 1)[1].split(' ')
      user = chunk[1]
      if (user[0] == "C"):
        this_time = datetime.datetime.strptime(chunk[2].split('[')[1], format_date)
        try:
            machine = obj[user]
        except KeyError, e:
            machine = obj.setdefault(user,{"init":this_time,"last":this_time,"downtime":0})
        last = machine["last"]
        diff = (this_time-last).total_seconds()
        if (diff > tick):
          machine["downtime"] += diff-tick
        machine["last"] = this_time

  except Exception:
    pass