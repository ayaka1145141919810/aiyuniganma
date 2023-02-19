import nltk
import string
from translate import Translator
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import re
import time
from translate import Translator
def tran(txt):
    # 实现英文转中文
    translator=Translator(to_lang='chinese')
    translation=translator.translate(txt)
    return translation
wnl = WordNetLemmatizer()
import requests

def main (query):
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
    res = requests.post(url, data=data).json()
    return res['translateResult'][0][0]['tgt']
with open('D:/mywords.txt','r')as f :
    tast = f.read()
    tast = tast.split('。')
stop = set(stopwords.words('english'))
global paragraph 
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None
with open ('D:/text.txt','r') as f:
    global paragraph
    paragraph = f.readlines()
    #print(paragraph)

translation = None
for i in paragraph:
    tokens = nltk.word_tokenize(i)
    tagged_sent = nltk.pos_tag(tokens)
    
    for j in tagged_sent:
        k= list(j)
        try:
            form = wnl.lemmatize( k[0],get_wordnet_pos(k[1]))
            if (form.lower() not in tast and 'NNP' not in k[1])and k[0].lower() not in tast:
                if '_' in k[0]:
                    ls =  k[0].split('_')
                    for v in ls:

                        tagged = nltk.pos_tag(v)
                        for y in  tagged:
                            form1 = wnl.lemmatize( y[0],get_wordnet_pos(y[1]))
                            if form1.lower() not in tast and (('NNP' not in y[1])or("'"not in y[1] )):
                                translation = tran(k[0])
                                print(form1,translation)
                            else:
                                pass
                elif "'" not in k[0] :

                    translation = tran(k[0])

                    print(form,translation)
                    #print(k[1])
        
        except:
            pass
        with open('D:/mm.txt','a+') as file:
            try:
                if translation != None:
                    file.write(k[0]+'('+translation+') ')
                else:
                    
                        file.write(k[0]+' ')
            except:
                pass
        translation = None



#global m




