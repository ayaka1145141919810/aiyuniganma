import re
with open('D:/all.json',encoding='UTF8') as f:
    json = f.read()
    tast = re.findall('"headWord":"(.*?)","content"',json)
    #print(a)
with open('D:/mywords.txt','a+')as f :
    tdf = '。'.join(tast)
    f.write(tdf)
import requests

def main(query):
    url = 'http://fanyi.youdao.com/translate'
    data = {
        "i": query,  # 待翻译的字符串
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "16081210430989",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    }
    
    res = requests.post(url, data=data)
    print(res.text)
    #print(res['translateResult'][0][0]['tgt']) ''' # 打印翻译后的结果

main('你好') # 输出: hello