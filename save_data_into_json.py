# Dummy data
date1 = "09/01/2019"
date2 = "10/01/2019"
date3 = "11/01/2019"
download = "78.60 Mbit/s"
upload = "9.89 Mbit/s"


import json

data = {}  
data['InternetSpeed'] = []  
data['InternetSpeed'].append([date1, download, upload])
data['InternetSpeed'].append([date2, download, upload])
data['InternetSpeed'].append([date3, download, upload])

print(data)

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)