import json
import requests

baseurl = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
api = "715f3f1b3c7b4408b551060356948ec0"
dic = {"api-key":api, "q": "University of Michigan"}
nyt_response = requests.get(baseurl, params = dic)
pythonobj = json.loads(nyt_response.text)


jsonfile = open("nyt.json", "w", encoding ="utf-8")
jsonfile.write(nyt_response.text)
jsonfile.close


for item in pythonobj['response']['docs']:
    print(item['headline']['main'])

CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    cache_diction = json.loads(cache_contents)
    cache_file.close()
except:
    cache_diction = {}

params_new = {"q": "University of Michigan"}

def params_unique_combination(baseurl, params, private_keys = [api]):
    alphabetized_keys = sorted(params_new.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
