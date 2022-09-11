import csv
import json
"""
with open('./data/neos.csv') as f:
    reader = csv.reader(f)
    next(reader)
    counter = 0
    for row in reader:
        if row[15] != '':
            counter += 1
    print(counter)
   
# => 1268

with open('./data/neos.csv') as f:
    reader = csv.reader(f)
    next(reader)
    counter = 0
    for row in reader:
        if row[4] != '':
            counter += 1
    print(counter)
   
# => 343

with open('./data/neos.csv') as f:
    reader = csv.reader(f)
    next(reader)
    counter = 0
    for row in reader:
        if row[4] == 'Apollo':
            diam = row[15]
    print(diam)
   
# => 1.5

with open('./data/neos.csv') as f:
    reader = csv.reader(f)
    next(reader)
    counter = 0
    for row in reader:
        counter += 1
    print(counter)
   
# => 23967
"""

with open('./data/cad.json') as f:
    contents = json.load(f)
    print(contents["count"])
    
# => 406785

with open('./data/cad.json') as f:
    contents = json.load(f)
    print(contents["count"])

# => 406785
