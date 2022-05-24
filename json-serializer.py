import json

def jsonCheck (string):
    bool = False
    try:
        jsonObject = json.loads(string)
        bool = True
    except:
        bool = False
    return bool



