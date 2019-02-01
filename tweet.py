import tweepy
import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.plotly as py

from plotly import tools

from dotenv import load_dotenv

import plotly
import datetime
import time  # {Added}

load_dotenv()


plotly.tools.set_credentials_file(
    username=os.environ.get('username'),
    api_key=os.environ.get('plotly_api_key'))


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

        trace_high = go.Scatter(
            x=df_store.Time,
            y=df_store['Download Speed'],
            name="Download Speed",
            line=dict(color='#17BECF'),
            opacity=0.8)
        trace_low = go.Scatter(
            x=df_store.Time,
            y=df_store['Upload Speed'],
            name="Upload Speed",
            line=dict(color='#7F7F7F'),
            opacity=0.8)

        data = [trace_high, trace_low]

        fig = tools.make_subplots(rows=1, cols=2)
        fig.append_trace(trace_high, 1, 1)
        fig.append_trace(trace_low, 1, 2)
        fig['layout'].update(
            height=600,
            width=800,
            title='Internet Speed for few months')
        py.iplot(fig, filename='simple-subplot-with-annotations')

        # Save plot as img
        py.image.save_as({'data': data}, 'scatter_plot', format='png')

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
