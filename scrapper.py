from googleapiclient.discovery import build
from functions import channel_dict, channel_df, comment_format, comments_csv, raw, video_csv
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('YOUTUBE_API_KEY')

try:
    youtube = build('youtube', 'V3', developerKey=api_key)

    # this code is to extract comments and replies
    def comment_scrapper(video_id, to_csv=False):
        try:
            video_id = video_id.split('v=')[1].split('&')[0]
            comment_data = []
            stat = youtube.commentThreads().list(
                part='id,snippet,replies',
                videoId=video_id)
            response = stat.execute()
            comments = comment_format(response, comment_data)

            while response.get('nextPageToken', None):
                stat = youtube.commentThreads().list(
                    part='id,snippet,replies',
                    videoId=video_id,
                    pageToken=response['nextPageToken'])
                response = stat.execute()
                comments = comment_format(response, comment_data)

            if to_csv:
                comments_csv(comments)
            return comments

        except Exception as e:
            return e


    # this code is to extract channel details
    def channel_details(channel_id, to_df=False, to_csv=False):
        try:
            stat = youtube.channels().list(
                part="id,snippet,statistics",
                id=channel_id)
            response = stat.execute()
            if to_csv:
                df = channel_df(channel_dict(response))
                df.set_index('ChannelName', inplace=True)
                df.to_csv('CSV/Channel_Details.csv')
            if to_df:
                return channel_df(channel_dict(response))
            else:
                return channel_dict(response)
        except Exception as e:
            return e


    # this code is to extract video details
    def video_details(video_id, to_df=False, to_csv=False):
        try:
            video_id = video_id.split('v=')[1].split('&')[0]
            stat = youtube.videos().list(
                part='snippet,statistics',
                id=video_id)
            response = stat.execute()
            details = raw(response)
            if to_csv:
                video_csv(details)
            if to_df:
                df = pd.DataFrame(details)
                return df
            else:
                return details
        except Exception as e:
            return e


    def youtube_scrap(quest, link, csv):
        try:
            if quest == "Channel Stats":
                if csv == "Yes":
                    return channel_details(link, to_csv=True)
                elif csv == "No":
                    return channel_details(link, to_csv=False)
            elif quest == "Comments":
                if csv == "Yes":
                    return comment_scrapper(link, to_csv=True)
                elif csv == "No":
                    return comment_scrapper(link, to_csv=False)
            elif quest == "Video Stats":
                if csv == "Yes":
                    return video_details(link, to_csv=True)
                elif csv == "No":
                    return video_details(link, to_csv=False)
        except Exception as e:
            return e

except Exception as e:
    print(f"An error occurred while connecting to the YouTube Data API: {str(e)}")
