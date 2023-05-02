import pandas as pd


# this will scrap comments and format it well
def comment_format(comments, comment_data):
    for comment in comments['items']:
        a = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        comment_data.append(a)
        if 'replies' in comment:
            a = comment['replies']['comments']
            for i in a:
                b = i['snippet']['textDisplay']
                comment_data.append(b)

    return comment_data


# this will turn comments data into a CSV
def comments_csv(data):
    df = pd.DataFrame(data)
    df.columns = ['comments']
    df.set_index('comments', inplace=True)
    df.to_csv('CSV/Comments.csv')


# this will take all channel data from api and extract necessary data from it
def channel_dict(raw_data):
    all_data = []
    for i in range(len(raw_data['items'])):
        data = dict(ChannelName=raw_data['items'][i]['snippet']['title'],
                    Subscribers=raw_data['items'][i]['statistics']['subscriberCount'],
                    Views=raw_data['items'][i]['statistics']['viewCount'],
                    TotalViews=raw_data['items'][i]['statistics']['videoCount'])
        all_data.append(data)

    return all_data


# this will convert channel data into dataframe for further use
def channel_df(channel_raw):
    channel_data = pd.DataFrame(channel_raw)
    channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
    channel_data['Views'] = pd.to_numeric(channel_data['Views'])
    channel_data['TotalViews'] = pd.to_numeric(channel_data['TotalViews'])
    return channel_data


# this will take all video data from api and extract necessary data from it
def raw(raw_data):
    all_data = []
    for i in raw_data['items']:
        data = dict(ChannelName =i['snippet']['channelTitle'],
                    VideoTitle =i['snippet']['title'],
                    ViewCount=i['statistics']['viewCount'],
                    LikeCount=i['statistics']['likeCount'],
                    FavouriteCount=i['statistics']['favoriteCount'],
                    CommentCount=i['statistics']['commentCount'])
        all_data.append(data)

    return all_data


# this will convert video data to a CSV
def video_csv(data):
    df = pd.DataFrame(data)
    df.set_index('ChannelName', inplace=True)
    df.to_csv('CSV/Video_details.csv')

