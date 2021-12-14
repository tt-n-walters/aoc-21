import requests
import json
import os


folder_name = os.path.dirname(os.path.abspath(__file__))


base_url = "https://adventofcode.com/2021/day/{}/input"
session_id = "53616c7465645f5f68f673c48e242e7693cb366dd5de0cd150bbd2aebf98a4c7dd52bc512d7cc085a3639c77abf751a4"


def cache(function):
    file = open(folder_name + "/cache.dat", "r")
    data = json.loads(file.read())
    file.close()

    def decorator(day):
        day = str(day)
        if day not in data:                   # Check if day has been downloaded previously
            input = function(day)             # If not, download and save
            data[day] = input
            file = open(folder_name + "/cache.dat", "w")
            file.write(json.dumps(data))
            file.close()
        return data[day]
    
    return decorator
            


@cache
def get_input(day):
    print("Downloading...")
    url = base_url.format(day)
    cookies = {
        "session": session_id
    }
    r = requests.get(url, cookies=cookies)
    return r.text
