import re
import requests
# def clear(text):
# 	return text.replace('\t','').replace('\n','')

def getSource(url):
	r = requests.get(url)
	return r.text

def stripHTML (source):
    source = re.sub('<style[^>]*?>[^<]*?<\/style>', '', source,flags=re.M|re.S|re.I)
    source = re.sub('<script[^>]*?>[^<]*?<\/script>', '', source,flags=re.M|re.S|re.I)
    source = re.sub('<!--.*?-->','',source,flags=re.M|re.S|re.I)
    source = re.sub('<[^<]+?>', '', source,flags=re.M|re.S|re.I)
    source = re.sub('\s+', ' ', source,flags=re.M|re.S|re.I)
    return source

html = getSource("https://thewebminer.com")
print(stripHTML(html))

