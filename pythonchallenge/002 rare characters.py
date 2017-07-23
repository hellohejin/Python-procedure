import urllib.request
import re
from collections import Counter

data = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode("utf-8")
pat = "\<!--(.*?)--\>"
rst = re.compile(pat,re.S).findall(data)
s = rst[1]
print(Counter(s))