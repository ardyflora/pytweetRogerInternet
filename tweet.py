import tweepy
import os
import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv
from datetime import date

import json
import pandas as pd
import datetime
import time # {Added}

load_dotenv()

# Authenticating twitter with credentials from env
auth = tweepy.OAuthHandler(os.environ.get('consumer_key'), os.environ.get('consumer_secret'))
auth.set_access_token(os.environ.get('access_token'), os.environ.get('access_token_secret'))
api = tweepy.API(auth)

# Running speedtest-cli to get download and upload speed of the Internet
process =  os.popen("speedtest-cli  --simple")
preprocessed = process.read()
process.close()

ping, download, upload, _ = preprocessed.split('\n')

#Expected vs Actual Speed
#message = "@Rogers, | Ignite 60 Plan | Actual Speed -  Download: {}, Upload: {}".format(download.split(':')[1], upload.split(':')[1])
message = "| Ignite 60 Plan | Actual Speed -  Download: {}, Upload: {}".format(download.split(':')[1], upload.split(':')[1])
#Posting message on twitter
api.update_status(message)


# Write into json file and plot the data
json_backup = 'internetSpeed.json'
df_store = pd.DataFrame(columns=["Time", "Download Speed", "Upload Speed"])
time_data = str(datetime.datetime.now())

try:
    df_store = pd.read_json(json_backup)

    df_store = df_store.append({
        "Time": time_data,
        "Download Speed": download.split(':')[1],
        "Upload Speed": upload.split(':')[1] 
    }, ignore_index=True)

    df_store.to_json(json_backup)
    print (df_store)    
except Exception as e:
    df_store = df_store.append({
        "Time": time_data,
        "Download Speed": download.split(':')[1],
        "Upload Speed": upload.split(':')[1]
        }, ignore_index=True)

    df_store.to_json(json_backup)

    # Plot is not working
    df_store.plot().bar()
    plt.savefig('new_speedtest.png')
