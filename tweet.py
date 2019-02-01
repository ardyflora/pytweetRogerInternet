import tweepy
import os
import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv

import pandas as pd
import datetime
import time  # {Added}

load_dotenv()


def twitter_authentication():
    # Authenticating twitter with credentials from env
    auth = tweepy.OAuthHandler(os.environ.get(
        'consumer_key'), os.environ.get('consumer_secret'))
    auth.set_access_token(os.environ.get('access_token'),
                          os.environ.get('access_token_secret'))
    return tweepy.API(auth)


def get_current_internet_speed():
    # Running speedtest-cli to get download and upload speed of the Internet
    process = os.popen("speedtest-cli  --simple")
    preprocessed = process.read()
    process.close()

    ping, download, upload, _ = preprocessed.split('\n')
    return download, upload


def write_into_json_file(download, upload):
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
        print(df_store)
    except Exception:
        df_store = df_store.append({
            "Time": time_data,
            "Download Speed": download.split(':')[1],
            "Upload Speed": upload.split(':')[1]
        }, ignore_index=True)

        df_store.to_json(json_backup)

        # Plot is not working
        df_store.plot().bar()
        plt.savefig('new_speedtest.png')


def main():
    api = twitter_authentication()
    download, upload = get_current_internet_speed()
    message = "| Ignite 60 Plan | Actual Speed -  Download: {}, Upload: {}".format(
        download.split(':')[1], upload.split(':')[1])

    # Update to twitter
    api.update_status(message)

    # write data into json
    write_into_json_file(download, upload)


if __name__ == "__main__":
    main()
