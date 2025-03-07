import requests, time

def getEvent(month, offset):
    api_url = 'https://api.api-ninjas.com/v1/historicalevents'
    with open('keys/history.txt', 'r', encoding='utf-16') as f:
        api_key = f.read().strip()
    final_list = []
    params={
        'month' : month,
        'offset' : offset
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