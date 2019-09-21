from urllib.request import urlopen
from json import *
from tabulate import tabulate
#http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=

def skinSetup():
    with open("skins.txt") as f:
        string = f.read()
        split= string.split("\n")
        split.remove("")
        ret = []
        for x in range(0,len(split),4):
            ret.append(split[x:x+4])
        return ret
def stickerSetup():
    with open("stickers.txt") as f:
        string = f.read()
        split= string.split("\n")
        split.remove("")
        ret = []
        for x in range(0,len(split),3):
            ret.append(split[x:x+3])
        return ret

def priceSetup(name):
    with urlopen(r"http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name="+name) as u:
        return  (loads(u.read())["lowest_price"])
def percent(x,y):
    return(str(round((x/y)*100))+"%")
skins = skinSetup()
stickers=stickerSetup()
prices = []
percentage = []
for x in range(len(skins)):
    name = (skins[x][0]+" ("+skins[x][2]+")").replace(" ","%20")
    percentage.append([float(priceSetup(name).replace("€","").replace(",",".").replace("-","0")),float(skins[x][1].replace(",","."))])
    prices.append(priceSetup(name))
for y in range(len(stickers)):
    name = stickers[y][0].replace(" ","%20")
    percentage.append([float(priceSetup(name).replace("€","").replace(",",".").replace("-","0")),float(stickers[y][1].replace(",","."))])
    prices.append(priceSetup(name))
prcnt = []
for x in percentage:
    prcnt.append(percent(*x))
table = [["name"],["buy price"],["current price",*prices],["percent",*prcnt],["info"]]
for skin in skins:
    table[0].append(skin[0]+" ("+skin[2]+")")
    table[1].append(skin[1]+"€")
    table[4].append(skin[3])
for sticker in stickers:
    table[0].append(sticker[0])
    table[1].append(sticker[1]+"€")
    table[4].append(sticker[2])
print(tabulate(table))
