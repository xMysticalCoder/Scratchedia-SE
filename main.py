from replit import db
import time

import os


def setup():
    charectarsVar = "qwertyuiopasdfghjklzxcvbnm 1234567890."
    global charectersList
    charectersList = list()
    for i in range(10):
        charectersList.append("")
    for i in range(len(charectarsVar)):
        charectersList.append(charectarsVar[i])


def encode(value):
    encoded = ""
    for i in range(len(value)):
        encoded = str(encoded) + str(charectersList.index(value[i]))
    return encoded


def decode(value):
    decoded = ""
    v = ' '.join(a + b for a, b in zip(value[::2], value[1::2]))
    v = v.split()

    for i in range(len(v)):
        decoded = str(decoded) + charectersList[int(v[i])]
    return decoded


def createTest(name, value):
    db[name] = value


Password = os.environ["Password"]

os.system("python -m pip install scratchclient")

from scratchclient import ScratchSession

createTest("test.se", "test1")
createTest("test2.se", "test2")

session = ScratchSession("xMysticalLegend", Password)
connection = session.create_cloud_connection(567384993)
setup()
while True:
    search = decode(connection.get_cloud_variable("Search"))
    try:
        result = db[search]
    except KeyError:
        result = "none"

    result = encode(result)

    connection.set_cloud_variable("Result", result)

    print(search)  # only for testing

    time.sleep(0.2)
