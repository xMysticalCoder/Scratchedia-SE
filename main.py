from replit import db

import os

Password = os.environ["Password"]

def install(library):
  os.system("python -m pip install " + library)
def uninstall(library):
  os.system("python -m pip uninstall " + library)

  
def setup():
  charectarsVar = "qwertyuiopasdfghjklzxcvbnm 1234567890"
  global charectersList
  charectersList = list()
  for i in range(10):
    charectersList.append("")
  for i in range(len(charectarsVar)):
    charectersList.append(charectarsVar[i])


def encode(value):
  encoded = ""
  for i in range(len(value)):
    encoded =str(encoded)+str(charectersList.index(value[i]))
  return encoded


def decode(value):
  decoded = ""
  v = ' '.join(a+b for a,b in zip(value[::2], value[1::2]))
  v = v.split()

  for i in range(len(v)):
    decoded = str(decoded) + charectersList[int(v[i])]
  return decoded

install("scratch2py")
uninstall("websocket-client")
install("websocker-client")
import scratch2py

s2py = scratch2py.s2py("xMysticalCoder", Password)

