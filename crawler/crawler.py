import requests
import re
import json
from bs4 import BeautifulSoup
import csv
import os, os.path

def get_amount_of_files_in_outputs():
    return len([name for name in os.listdir('./outputs/') if os.path.isfile(os.path.join('./outputs/', name))])

#TODO: Logic that handles situations where the query fails. Message or re-run.

def start(filename):
    search_words_file = open(filename, 'r')
    search_words = search_words_file.readlines()
    file_amount = get_amount_of_files_in_outputs()

    for word in search_words[file_amount:]:
        get_video_data_by_word(word.strip())


def get_video_data_by_word(query):
    x = requests.get(f"https://www.youtube.com/results?search_query={query}")
    soup = BeautifulSoup(x.content, 'html.parser')

    script_tags = soup.find_all('script')

    for script_tag in script_tags:
        script_content = script_tag.string

        if script_content:
            matches = re.findall(
                r'var\s+ytInitialData\s*=\s*{(.*?)};', script_content, re.DOTALL)

            if len(matches) == 1:
                parse_json_to_csv_file(query, f"{'{'}{matches[0]}{'}'}")


def parse_json_to_csv_file(query, json_data):
    print(f'Starting to save query: {query}')
    data = json.loads(json_data)

    field_names = ['Video Id', 'Title', 'View Count', 'Length', 'Channel']

    video_data = data['contents']['twoColumnSearchResultsRenderer']['primaryContents'][
        'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

    videos = ({
        "Video Id": vid['videoRenderer']['videoId'],
        "Title": vid['videoRenderer']['title']['runs'][0]['text'],
        "View Count": vid['videoRenderer']['viewCountText']['simpleText'],
        "Length": vid['videoRenderer']['lengthText']['simpleText'],
        "Channel": vid['videoRenderer']['ownerText']['runs'][0]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
    }
        for vid in video_data if 'videoRenderer' in vid)
    
    with open(f'outputs/{query}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(videos)

start('./20k.txt')