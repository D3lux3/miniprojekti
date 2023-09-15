import requests
import re
import json
from bs4 import BeautifulSoup
import csv
import os
import os.path
import sys

search_arg = ""
name_arg = ""

if len(sys.argv) > 1:
    query_arg = "&sp=CAM%253D"
    name_arg = "_most_watched"

def get_amount_of_files_in_outputs():
    return len([name for name in os.listdir('./outputs/') if os.path.isfile(os.path.join('./outputs/', name))])

# TODO: Logic that handles situations where the query fails. Message or re-run.


def start(filename):
    search_words_file = open(filename, 'r')
    search_words = search_words_file.readlines()
    file_amount = get_amount_of_files_in_outputs()

    for word in search_words[file_amount:]:
        get_video_data_by_word(word.strip())


def get_video_data_by_word(query):
    x = requests.get(f"https://www.youtube.com/results?search_query={query}{query_arg}")
    soup = BeautifulSoup(x.content, 'html.parser')

    script_tags = soup.find_all('script')

    for script_tag in script_tags:
        script_content = script_tag.string

        if script_content:
            matches = re.findall(
                r'var\s+ytInitialData\s*=\s*{(.*?)};', script_content, re.DOTALL)

            if len(matches) == 1:
                parse_json_to_csv_file(query, f"{'{'}{matches[0]}{'}'}")


def map_video_data(video):
    video_renderer = video.get('videoRenderer', {})
    vid_id = video_renderer.get('videoId', '')
    title = video_renderer.get('title', {}).get('runs', [{}])[0].get('text', '')
    view_count = video_renderer.get('viewCountText', {}).get('simpleText', '')
    length = video_renderer.get('lengthText', {}).get('simpleText', '')
    owner_text = video_renderer.get('ownerText', {}).get('runs', [{}])[0]
    channel = owner_text.get('navigationEndpoint', {}).get('commandMetadata', {}).get('webCommandMetadata', {}).get('url', '')
    return {
        "Video Id": vid_id,
        "Title": title,
        "View Count": view_count,
        "Length": length,
        "Channel": channel
    }


def parse_json_to_csv_file(query, json_data):
    print(f'Starting to save query: {query}{name_arg}')
    data = json.loads(json_data)

    field_names = ['Video Id', 'Title', 'View Count', 'Length', 'Channel']

    video_data = data['contents']['twoColumnSearchResultsRenderer']['primaryContents'][
        'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

    videos = (map_video_data(vid) for vid in video_data if 'videoRenderer' in vid)

    with open(f'outputs/{query}{name_arg}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(videos)


start('./20k.txt')
