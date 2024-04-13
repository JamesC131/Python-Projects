import pyshorteners

link = input("")
shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short(link)