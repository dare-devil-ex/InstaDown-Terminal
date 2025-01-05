# Author: @dare-devil-ex
# Reminder: Changing credits doesn't make you a programmer ;)

try:
    from bs4 import BeautifulSoup as bs
    import cloudscraper
    from datetime import datetime as dt
    import re
    from wget import download as dl
    from time import sleep
    from colorama import Fore
    from os import system as wkaie
    from webbrowser import open as o
except:
    wkaie("pip install colorama")
    wkaie("pip install cloudscraper")
    wkaie("pip install bs4")
    wkaie("cls")

g = Fore.GREEN
c = Fore.CYAN
b = Fore.BLUE
y = Fore.YELLOW
w = Fore.WHITE
r = Fore.RED
p = Fore.MAGENTA

clock = dt.now().strftime("%I%M%S%f")
ddex = cloudscraper.create_scraper()
holder = []
    
class Wkaie:
    def banner():
        banner = """░█──░█ ░█─▄▀ ─█▀▀█ ▀█▀ ░█▀▀▀ \n░█░█░█ ░█▀▄─ ░█▄▄█ ░█─ ░█▀▀▀ \n░█▄▀▄█ ░█─░█ ░█─░█ ▄█▄ ░█▄▄▄"""
        print(banner, "\n\n")
    
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
        print("{}Cover: {}{}{}".format(g, c, cover, w))
        o(cover)
        sleep(1)
        o(vid)
    elif msg == 2:
        for count, Purl in enumerate(holder, start=1):
            print("{}Post {}{}{}: {}{}{}".format(w, b, count, w, y, Purl, w))
            o(Purl)
            sleep(0.7)
            print()
        holder.clear()
    else:
        wkaie("cls")
        print("Only Instagram links\nCheck the link again", w)
        exit(0)

try:
    wkaie("cls")
    while True:
        Wkaie.banner()
        Wkaie.Process(input(f"Enter the url: {p}"))
        worker()
except KeyboardInterrupt:
    wkaie("cls")
    print(r, "Program exited")
    print(c, "Author:", g, "@dare-devil-ex\n", w)
    o("https://github.com/dare-devil-ex")