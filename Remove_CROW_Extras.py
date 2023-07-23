import os
import json
import re
import csv
directory = 'CROW'
for subdir, dirs, files in os.walk(directory):
  for filename in os.listdir(subdir):
    print(filename)
    f = os.path.join(subdir, filename)
    print(f)
    # checking if it is a file

    if os.path.isfile(f):
    	if(f.endswith(".txt") and not os.path.getsize(f) == 0):
            with open(f, "r+") as f:
                wsstart = False
                d = f.readlines()
                f.seek(0)
                for i in d:
                    print(i.lower())
                    print(i != "")
                    if "works cited" in i.lower() or "references" in i.lower():
                        print(i.lower())
                        wsstart = True
                    if i[0] != '<' and not i.isspace() and not wsstart:
                        f.write(i)
                f.truncate()
