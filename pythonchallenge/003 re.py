import urllib.request
import re

data = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode("utf-8")
pat = "[^A-Z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][^A-Z]"
rst = re.compile(pat).findall(data)
print(''.join(rst))