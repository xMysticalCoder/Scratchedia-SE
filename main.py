from replit import db

import os

def install(library):
  os.system("python -m pip install " + library)
def uninstall(library):
  os.system("python -m pip uninstall " + library)

install("scratch2py")
uninstall("websocket-client")
install("websocker-client")
