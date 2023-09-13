import json

with open('test.json') as f:
    data = json.load(f)

videos = data['contents']['twoColumnSearchResultsRenderer']['primaryContents'][
    'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

for video in videos:
    if 'videoRenderer' not in video:
        continue

    videoId = video['videoRenderer']['videoId']
    title = video['videoRenderer']['title']['runs'][0]['text']
    view_count = video['videoRenderer']['viewCountText']['simpleText']
    length = video['videoRenderer']['lengthText']['simpleText']

    print(f"Video ID: {videoId}")
    print(f"Title: {title}")
    print(f"View Count: {view_count}")
    print(f"Length: {length}")
    print()
