from urllib.request import urlopen
from json import *
from tabulate import tabulate
notes = []
def setup():
    with open(r"C:\Users\Castor\Desktop\steamPrice\skins.txt") as mine:
        z = []
        for x in mine.read().split("\n"):
            if(x != ""):
                z.append(x)
        y = []
        for i in range(0, len(z), 4):
            y.append(z[i:i+4])
    return(y)


def getprices(name):
    returns = []
    with urlopen(r"http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name="+ name.replace(" ", "%20")) as f:
        returns.append(loads(f.read())["lowest_price"])
    return(returns)

def percent(x,y):
    return(str(round((x/y)*100))+"%")
stuff = setup()
pricesOld = []
pricesNew = []
for x in range(len(stuff)):
    pricesOld.append(stuff[x][1]+"€")
    pricesNew.append(*getprices(stuff[x][0]+" ("+stuff[x][2]+")"))
    notes.append(stuff[x][3])
tbl = []
v = []
uglycode = []
for x in stuff:
    v.append(x[0])
v.insert(0, "NAME")
tbl.append(tuple(v))
v=[]
everymoreuglycode=[]
for x in pricesOld:
    v.append(x)
uglycode.append(v)
#v.insert(0, "BOUGHT")
tbl.append(tuple(["BOUGHT"]+v))
v=[]

for x in pricesNew:
    v.append(x)

uglycode.append(v)
#v.insert(0, "CURRENT")
tbl.append(tuple(["CURRENT"]+v))

for x in range(len(uglycode[0])):
    everymoreuglycode.append(percent(float(uglycode[1][x].replace("€", "").replace(",", ".").replace("-","0")), float(uglycode[0][x].replace("€", "").replace(",", ".").replace("-","0"))))
everymoreuglycode.insert(0, "PERCENT")
tbl.append(tuple(everymoreuglycode))
tbl.append(tuple(["NOTES"]+notes))

print(tabulate(tbl))

input()
