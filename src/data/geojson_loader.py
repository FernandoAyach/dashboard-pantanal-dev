import json
import urllib.request

def load_geojson(url):
    with urllib.request.urlopen(url) as response:
        return json.load(response)
