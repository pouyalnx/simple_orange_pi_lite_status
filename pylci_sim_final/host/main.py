from bottle import run,route,Bottle,template,request
from os import path
import json
import logging
import sys


addr=(path.dirname(__file__) or '.')+'/'
parent="/"
menu={}
app=Bottle()

def create_menu():
    global parent
    pass


@app.route('/')
def main():
    jdata=json.dumps({'menu':menu})
    
    if request.query.get('json','false').lower()=='true':
        return jdata
    
    with open(addr+'main.html') as f:
        return template(f.read(),menu=menu,jdata=jdata)
        


if __name__=="__main__":
    logging.basicConfig(filename=addr+'main.log',format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    
    with open(addr+'main.json') as f:
        dat=json.load(f)
    print(dat)
    for app_name,app_addr in dat.items():
        try:
            sys.path.append(app_addr)    
            apx=__import__(app_name)
            apx.init(parent)
            app.mount(app_name,apx.app)
            menu[app_name]=parent+app_name
            logging.info("loaded "+app_name)
        except:
            logging.info("unable to load "+app_name)
    menu["back"]=parent
    

    run(app)







