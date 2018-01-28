#!/usr/bin/python
import sys
from datetime import datetime

import pytz

def dt_utc_str_to_local(hour):
  dt = datetime.now()
  dt = dt.replace(hour=hour, tzinfo=pytz.timezone('UTC'))
  return dt.astimezone(pytz.timezone('US/Pacific')).strftime('%I %p US/Pacific')

print dt_utc_str_to_local(int(sys.argv[1]))
