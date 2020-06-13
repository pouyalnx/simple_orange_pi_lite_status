from bottle import Bottle,redirect,route,run,template,request
import json
import logging
import time
from os import path

app=Bottle()
addr=(path.dirname(__file__) or '.')+'/'
parent="/"
menu={}



def init(parent_addr):
    global menu
    parent=parent_addr
    with open(addr+'main.json') as f:
        dat=json.load(f)
    

    
    for app_name,app_addr in dat.items():
        try:
            apx=__import__(addr+app_addr)
            apx.init(parent)
            app.mount(app_name,apx.app)
            menu[app_name]=parent+app_name
            logging.info("loaded "+app_name)
        except:
            logging.error("unable to load "+app_name)
    menu["back"]=parent

    return True



@app.route('/')
def main():
    data=str(time.ctime())
    jdata=json.dumps({'menu':menu,'data':data})
    
    if request.query.get('json','false').lower()=='true':
        return jdata
    
    with open(addr+'main.html') as f:
        return template(f.read(),menu=menu,jdata=jdata,data=data)
        

if __name__=="__main__":
    init("/")
    run(app)