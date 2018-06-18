import sys
import requests
import os
from pymongo import MongoClient
import pprint


def runAttack(codigo,parametros):
  pass

def cargarBaseDeDatos(codigo):
  client = MongoClient('mongodb://localhost:27017/')
  db = client['ORCE']
  collection = db[codigo]
  parametros = []
  for parametro in collection.find():
    parametros.append(parametro)
  if(len(parametros) == 0):
    print("NEL")
    for i in range(10,100,5):
      parametros.append({
        "inicio":i*10000,
        "primerNoUsado":i*10000
      })
  print(parametros)   
  runAttack(codigo, parametros)

if __name__ == '__main__':
  codigo = sys.argv[1]
  if(len(codigo)!=9):
    print("Codigo No valido")
    exit()
  print('Iniciando ataque a '+ codigo)
  cargarBaseDeDatos(codigo)

