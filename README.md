# Python-Scripts

#Strip Html code from string.

    def stripHTML (source):
        #remove style
        source = re.sub('<style[^>]*?>[^<]*?<\/style>', '', source,flags=re.M|re.S|re.I)
        #remove scripts
        source = re.sub('<script[^>]*?>[^<]*?<\/script>', '', source,flags=re.M|re.S|re.I)
        #remove comments
        source = re.sub('<!--.*?-->','',source,flags=re.M|re.S|re.I)
        #remove all html tags
        source = re.sub('<[^<]+?>', '', source,flags=re.M|re.S|re.I)
        #remove multiple spaces
        source = re.sub('\s+', ' ', source,flags=re.M|re.S|re.I)
        return source
    
    html = getSource("https://thewebminer.com")
    print(stripHTML(html))


