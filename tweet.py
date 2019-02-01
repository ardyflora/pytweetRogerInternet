import tweepy
import os
import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv

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
    time_data = str(datetime.datetime.now().strftime("%Y-%m-%d"))

    try:
        df_store = pd.read_json(json_backup)

        df_store = df_store.append({
            "Time": time_data,
            "Download Speed": float(download.split(':')[1].split()[0]),
            "Upload Speed": float(upload.split(':')[1].split()[0])
        }, ignore_index=True)

        df_store.to_json(json_backup)

        # Plot is not working
        #plt.scatter(df_store['Time'].tolist(), df_store['Download Speed'], df_store['Upload Speed'])
        # plt.savefig('new_speedtest.png')

        plt.plot(
            df_store['Time'].tolist(),
            df_store['Download Speed'],
            color='g')
        plt.plot(
            df_store['Time'].tolist(),
            df_store['Upload Speed'],
            color='orange')
        plt.xlabel('Date')
        plt.ylabel('Internet Speed')
        plt.title('Upload and Download Internet Speed')

        ax = plt.gca()

        # recompute the ax.dataLim
        ax.relim()
        # update ax.viewLim using the new dataLim
        ax.autoscale_view()

        plt.savefig('new_speedtest.png')

    except Exception as e:
        print("The error msg:", e)


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
