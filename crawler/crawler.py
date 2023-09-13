import requests
import re
from bs4 import BeautifulSoup
import json

x = requests.get('https://www.youtube.com/results?search_query=asd')

soup = BeautifulSoup(x.content, 'html.parser')


script_tags = soup.find_all('script')

videos = []

# Iterate through each <script> tag and search for the JavaScript object
for script_tag in script_tags:
    # Get the text content of the script tag
    script_content = script_tag.string
    if script_content:
        # Use regular expressions to search for "videoRenderer" properties and their values
        matches = re.finditer(r'"videoRenderer":\s*({[^}]+})', script_content)

        for match in matches:
            # Extract and parse the JSON object
            m = match.group(1)
            print(m)

            json_data = json.loads(m)
            # Append the "videoRenderer" property and its value
            videos.append(json_data["videoRenderer"])

# Print the extracted "videoRenderer" properties and their values
for video_renderer in videos:
    print("Video Renderer:")
    print(json.dumps(video_renderer, indent=4))
