import json

with open('test.json') as f:
    data = json.load(f)

videos = data['contents']['twoColumnSearchResultsRenderer']['primaryContents'][
    'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

# Maybe faster to implement regex that gets contents instead of the whole JSON.

videos_2 = ({
    "videodId": vid['videoRenderer']['videoId'],
    "title": vid['videoRenderer']['title']['runs'][0]['text'],
    "view_count": vid['videoRenderer']['viewCountText']['simpleText'],
    "length": vid['videoRenderer']['lengthText']['simpleText'],
    "channel": vid['videoRenderer']['ownerText']['runs'][0]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
}
    for vid in videos if 'videoRenderer' in vid)


for v in list(videos_2):
    videoId, title, view_count, channel, length = v.values()
    print(f"Video ID: {videoId}")
    print(f"Title: {title}")
    print(f"View Count: {view_count}")
    print(f"Channel: {channel}")
    print(f"Length: {length}")
    print()