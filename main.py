import time, datetime
from otvetmailru import OtvetClient
import parse
import json






if __name__ == '__main__':
    with open('config.json', 'r') as f:
        data = json.loads(f.read())
    while True:
        try:
            client = OtvetClient()
            client.authenticate(data['mailru'][0]['login'], data['mailru'][0]['password'])
            if client.check_authentication() == True:
                parse.parse(client, data['mindsdb'][0]['session'], data['mindsdb'][0]['sql_queries'])
            else:
                print(f'{datetime.datetime.now()}  |  check_authentication() = False')
                with open('textdata/errors.txt', 'a+') as err:
                    print(f'{datetime.datetime.now()}  |  check_authentication() = False', file=err)
        except Exception as e:
            print(f'{datetime.datetime.now()}  |  {e}')
            with open('textdata/errors.txt', 'a+') as err:
                print(f'{datetime.datetime.now()}  |  {e}', file=err)
            time.sleep(5)
            continue




