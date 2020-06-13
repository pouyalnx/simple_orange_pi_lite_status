from bottle import Bottle,redirect,route,run,template,request
import json
import logging
import time
from os import path
from os import popen

app=Bottle()
addr=(path.dirname(__file__) or '.')+'/'
parent="/"
menu={}



def init(parent_addr):
    global menu
    parent=parent_addr
    menu["back"]=parent

    return True



@app.route('/')
def main():
    data=popen("hostnamectl").read()
    data+=popen("iwconfig").read()
    data+=popen("ifconfig").read()
    jdata=json.dumps({'menu':menu,'data':data})
    if request.query.get('json','false').lower()=='true':
        return jdata
    with open(addr+'index.html') as f:
        return template(f.read(),menu=menu,jdata=jdata,data=data)
        

if __name__=="__main__":
    init("/")
    run(app)