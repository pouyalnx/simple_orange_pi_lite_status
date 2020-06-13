import requests
import json
import re
import time

url='/'
url_undo='/'
url_base='http://localhost:8080'

url_query='?json=true'
error_repeat_flag=False


while True:
    try:
        page=requests.get(url_base+url+url_query)
        data=json.loads(page.text)
        page.close()
        error_repeat_flag=False


        print("************************************************************")
        if 'data' in data.keys():
            print(data['data'])
        if 'menu' in data.keys():
            for a,b in data['menu'].items():
                print(a)
            
            loc=input()
            if loc in data['menu'].keys():
                url_undo=url
                url=data['menu'][loc]
            elif loc=='exit':
                break
    except KeyboardInterrupt:
        print("good bye")
    except:
        print("error:unable to get data from web page")
        url=url_undo
        if error_repeat_flag:
            time.sleep(1)
        error_repeat_flag=True










