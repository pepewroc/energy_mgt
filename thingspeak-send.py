import requests as rq

def_url="https://api.thingspeak.com/update?api_key=YDJHUDWKT904EFMF"

def setUrl( thgurl="https://api.thingspeak.com/update?api_key=YDJHUDWKT904EFMF") :
    def_url=thgurl


def senddata(vars: list, where_url: str) :
    # process list of arg to url syntax
    url_postfix=where_url + "?"
    for idx, elm in enumerate(vars) :
        print(idx,elm)
        url_postfix+="&" if idx > 0 else ""
        url_postfix+="field"+str(idx+1)+"="+str(elm)
    print(url_postfix)
    # open http channel
    resp=rq.get(url_postfix)
    if resp.status_code == 200 :
        return 0
    else :
        return 255



l=[1, 34,3.4,56.677]
setUrl()
print(senddata(l, def_url))
