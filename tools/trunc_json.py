import datetime
import json
import sys
import tools

if not (len(sys.argv) == 3):
    print("First argument is filename and second argument is a date(YYYY-MM-DD) to truncate to.")
    sys.exit()

filename = sys.argv[1]

def string_to_date(daystring):
    return datetime.datetime.strptime(daystring, "%Y-%m-%d").date()


curdate = string_to_date(sys.argv[2])
cached = tools.parse_cached_json(filename)
for daystring in list(cached['json'].keys()):
    if string_to_date(daystring) > curdate:
        cached['json'].pop(daystring, None)

with open(filename, 'w') as file:
    json.dump(cached['json'], file)
