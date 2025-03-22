import requests, time, random

def getEvent(month, offset, year=1900):
    api_url = 'https://api.api-ninjas.com/v1/historicalevents'
    with open('NYT_Flashbacks/app/keys/history.txt', 'r', encoding='utf-16') as f:
        api_key = f.read().strip()
    final_list = []
    if year + 10 < 2020:
        max_year = year+10
    else:
        max_year = 2020
    min_year = year -10
    params={
        'month' : month,
        'offset' : offset,
        'year' : random.randint(min_year, max_year)
    }
    # Replace 'YOUR_API_KEY' with your actual API key
    response = requests.get(api_url, headers={'X-Api-Key': api_key}, params=params)

    if response.status_code == requests.codes.ok:
        # Parse the JSON response
        historical_events = response.json()
        print(historical_events)
        return [historical_events[0]['year'], historical_events[0]['event']]
    else:
        print("Error:", response.status_code, response.text)
