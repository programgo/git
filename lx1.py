import requests
import json

def test_get():
    corpid = 'ww20eb183966e6f314'
    corpsecret = 'e4mFLh5Nwzsp8Zi7hPHFiqAX6uOblVq1yV5hGSBcx54'
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    print(r.json()['access_token'])
    return r.json()['access_token']
def test_create():
    data = {
    "userid": "zhangsangouzi",
    "name": "张三",
    "mobile": "13800000001",
    "department": [1],
    }
    str = test_get()
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token='+ str
    print(url)
    res = requests.post(url,json=data)
    print(res.json())
def test_read():
    readmem = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get()}&userid=zhangsan')
    print(readmem.json())
def test_update():
    data = {
    "userid": "zhangsangouzi",
    "name": "张二狗",
    "mobile": "13800000001",
    }
    gengxin = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_get()}',json=data)
    print(gengxin.json())
def test_delete():
    shanchu = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get()}&userid=zhangsan')
    print(shanchu.json())

if __name__ == "__main__":
    test_delete()

