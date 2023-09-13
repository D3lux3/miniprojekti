import requests
import re
import json
from bs4 import BeautifulSoup

x = requests.get('https://www.youtube.com/results?search_query=asd')

soup = BeautifulSoup(x.content, 'html.parser')

pattern = 'var\s+ytInitialData\s*=\s*{(.*?)};'


script_tags = soup.find_all('script')

for script_tag in script_tags:
    script_content = script_tag.string

    if script_content:
        # Use regular expressions to search for the JavaScript object
        matches = re.findall(r'var\s+ytInitialData\s*=\s*{(.*?)};', script_content, re.DOTALL)

        if len(matches) == 1:
            f = open("test.json", "a")
            f.write(f"{'{'}{matches[0]}{'}'}")
            f.close()