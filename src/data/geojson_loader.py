import json
import urllib.request

def carregar_geojson(url):
    with urllib.request.urlopen(url) as response:
        return json.load(response)
