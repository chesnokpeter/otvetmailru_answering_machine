import requests






def questions_togpt(title, description, session, queries):
    url = 'https://cloud.mindsdb.com/api/sql/query'
    cookies = {'session': session}
    response = requests.post(url, json={'query': 
                        f'{queries}\'{title}\n{description}\';'}, cookies=cookies)
    gptanswer = response.json()['data'][0][0]
    return gptanswer


