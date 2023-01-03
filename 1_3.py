from bs4 import BeautifulSoup
import requests
import json
import re
from user_agent import generate_user_agent
import time
from random import uniform


def parse_hh(title='python разработчик',n_pages=100):
    data={"data":[]}
    title=str(title).replace(' ',"+")
    page=19
    for page in range(n_pages):
        search = f"https://hh.ru/search/vacancy?text={title}&page={page}&"
        search += "&salary=&currency_code=RUR&experience=doesNotMatter&"
        search += "order_by=publication_time&search_period=0&items_on_page=20"
        search = search.replace(' ','')
        headers = {'User-Agent':
                       generate_user_agent(device_type="desktop",
                                           os=('mac', 'linux'))}
        try:
            r = requests.get(search,timeout=3, headers=headers)
        except Exception as e: print("Error with url: "+search+" \n"+str(e))

        page_content = BeautifulSoup(r.content, "lxml")#"html.parser")
        page_content = page_content.find('div',
                                         attrs={"class":"vacancy-serp-content"})
        page_content = page_content.find_all(attrs={"class":"serp-item__title"})
        urls = [c.attrs["href"] for c in page_content]
        time.sleep(uniform(0.5,1.5))
        url=urls[0]
        #url='https://hh.ru/vacancy/67644659?from=vacancy_search_list&hhtmFrom=vacancy_search_list&query=python%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA'
        for url in urls:
            try:
                r = requests.get(url,timeout=3, headers=headers)
                page_content = BeautifulSoup(r.content, "lxml")
                tit_tmp = page_content.find(attrs={"data-qa":
                                                       "vacancy-title"}).text
                sal_tmp = page_content.find(attrs={"data-qa":
                                                       "vacancy-salary"}).text
                exp_tmp = page_content.find(attrs={"data-qa":
                                                       "vacancy-experience"}).text
                try:
                    reg_tmp = page_content.find(attrs={"data-qa":
                                                           "vacancy-view-location"}).text
                except:
                    try:
                        reg_tmp = page_content.find(attrs={"data-qa":
                                                               "vacancy-view-raw-address"}).text
                    except:
                        try:
                            reg_tmp = page_content.find(attrs={"data-qa":
                                                                   "vacancy-view-link-location"}).text
                        except:
                            reg_tmp = ""
                data["data"].append({"title":tit_tmp,"work experience":exp_tmp,
                                     "salary":sal_tmp,"region":reg_tmp})
                with open('data.json','w') as file:
                    json.dump(data,file)

            except Exception as e:
                print("Error with url: "+url+" \n"+str(e))

            time.sleep(uniform(0.3,0.7))
        print("Page = ",page,"  Data length = ",len(data["data"]))

    return data

parse_hh()


def is_palindrome(s:str='taco cat'):
    s=s.lower()
    s=re.sub('[^a-z0-9а-яё]','',s)
    #s=str(s).replace(' ','')
    return s == s[::-1]

s='Лазер Боре   Р обрезал '
print(s,is_palindrome(s))
s='Лазер Боре    обрезал'
print(s,is_palindrome(s))



def int_to_Latin(i:int=1945):

    #i=1945
    d_Int_Lat={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',
               10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',
               100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',
               900:'CM',1000:'M',2000:'MM',3000:'MMM',0:''}
    m=int(i/1000)*1000
    h=int(i/100)*100-m
    d=int(i/10)*10-m-h
    n=i-m-h-d
    return d_Int_Lat[m]+d_Int_Lat[h]+d_Int_Lat[d]+d_Int_Lat[n]

i=1945
print(i,int_to_Latin(i))
i=257
print(i,int_to_Latin(i))
i=25
print(i,int_to_Latin(i))
i=8
print(i,int_to_Latin(i))



def check_brackets(s:str='{[}]'):
       #s='{{(()())}}'
    open_br = set(['(','[','{'])
    close_br = set([')',']','}'])
    relation_br={'(':')','[':']','{':'}'}
    st0=''
    bOk=True
    for c in s:
        #print(c)
        if c in open_br:
            st0+=c
        elif c in close_br:
            if len(st0)>0:
                if c == relation_br[st0[-1]]:
                    st0=st0[:-1]
                else:
                    bOk=False
                    break
            else:
                bOk=False
                break
    return bOk

s='{{(()())}}()'
print(s,check_brackets(s))
s='{[}]'
print(s,check_brackets(s))



def bin_to_int(a:str='1001',b:str='01101'):
    a=int(a, 2)
    b=int(b, 2)
    return format(a*b, 'b')

print(bin_to_int('10','11'))
print(bin_to_int('10100','10011'))