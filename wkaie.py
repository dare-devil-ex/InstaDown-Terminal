try:
    from bs4 import BeautifulSoup as bs
    import cloudscraper
    from datetime import datetime as dt
    import re
    from random import choice
    from colorama import Fore, Back
    from os import system as wkaie
except:
    wkaie("pip install colorama")
    wkaie("pip install cloudscraper")
    wkaie("pip install bs4")
    wkaie("cls")

g = Fore.GREEN
c = Fore.CYAN
b = Fore.BLUE
w = Fore.WHITE
p = Fore.MAGENTA

clock = dt.now().strftime("(%Y | %b | %a)[%I:%M:%p]\t\t")
ddex = cloudscraper.create_scraper()
holder = []

def banner():
    color = [g, c, p, b, w]
    banner = """░█──░█ ░█─▄▀ ─█▀▀█ ▀█▀ ░█▀▀▀ 
    ░█░█░█ ░█▀▄─ ░█▄▄█ ░█─ ░█▀▀▀ 
    ░█▄▀▄█ ░█─░█ ░█─░█ ▄█▄ ░█▄▄▄"""
    
    print()
    
class Wkaie:
    def downReel(key):
        global vid, cover, conn
        conn = 0
        instaUrl = "https://imginn.com/p/" + key + "/"
        try:
            if ddex.get(instaUrl).status_code == 200:
                conn = 0
                wkan = ddex.get(instaUrl).content
                finalStr = bs(wkan, "lxml").find("video")
                vid = finalStr['src']
                cover = finalStr['poster']
        except Exception as e:
            conn = 1
            print("Error:", e)
     
    def downPost(key):
        global conn
        conn = 0
        instaUrl = "https://imginn.com/p/" + key + "/"
        try:
            if ddex.get(instaUrl).status_code == 200:
                conn = 0
                wkan = ddex.get(instaUrl).content
                finalStr = bs(wkan, "lxml")
                for row in finalStr.findAll("div", attrs={"class": "media-wrap"}):
                    wkimgT = row.find("img")
                    wkvidT = row.find("video")
                    if wkimgT:
                        wkimgSrc = wkimgT.get('src', None)
                        if wkimgSrc == "//assets.imginn.com/img/lazy.jpg":
                            wkimgSrc = wkimgT.get('data-src', None)
                        if wkimgSrc:
                            holder.append(wkimgSrc)
                    
                    if wkvidT:
                        wkvidSrc = wkvidT.get('src', None)
                        if wkvidSrc:
                            holder.append(wkvidSrc)
        except Exception as e:
            conn = 1
            print("Error:", e)

    def Process(_url):
        global msg
        msg = 0
        try:
            if re.findall("instagram.com", _url):
                if re.findall("/reel/", _url):
                    msg = 1
                    process = str(_url.split("/reel/")[1]).split("/")[0]
                    Wkaie.downReel(process)
                if re.findall("/p/", _url):
                    msg = 2
                    process = str(_url.split("/p/")[1]).split("/")[0]
                    Wkaie.downPost(process)
                
                
            else:
                msg = 0
        except Exception as e:
            print("Error: ", e)
            
def worker():
    if msg == 1:
        print("{}Video Url: {}{}{}\n".format(g, c, vid, w))
        print("Cover: {}".format(cover))
    elif msg == 2:
        for c, Purl in enumerate(holder, start=1):
            print("Post {}: {}\n".format(c, Purl))
        holder.clear()
    else:
        wkaie("cls")
        print("Only Instagram links\nCheck the link again")

wkaie("cls")
banner()
Wkaie.Process(input("Enter the url: "))
worker()