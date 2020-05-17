import requests 
import urllib.request 
import time

dates = ['26', '05']
for i in dates: 
    download_url = "'http://web.mta.info/developers/data/nyct/turnstile/turnstile_1805' + i + '.txt'" 
    print(download_url) 
    urllib.request.urlretrieve(download_url, dirpath + '/' +i) 
    time.sleep(1)


from os import listdir 
from os.path import isfile, join 
onlyfiles = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]

import csv 
content = []

for file in onlyfiles: 
    with open(file, 'r', newline='\n') as source_file: 
        for line in csv.reader(source_file, delimiter='\n'): 
            content.append(line[0])
            
with open('combined.txt', 'w') as target_file: 
    for line in content: 
        target_file.write(line + '\n')