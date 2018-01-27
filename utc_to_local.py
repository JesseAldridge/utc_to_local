import sys
from datetime import datetime

import pytz

def dt_utc_str_to_local(dt_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d_%H.%M.%S')
    dt = dt.replace(tzinfo=pytz.timezone('UTC'))
    return dt.astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %I:%M %p')

print dt_utc_str_to_local(' '.join(sys.argv[1:]))
