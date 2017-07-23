import urllib.request
import re
import time

def crawl(nothing):
	try:
		url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+str(nothing)
		data = urllib.request.urlopen(url).read().decode("utf-8")
		time.sleep(0.5)
		rst = re.compile('\d+').findall(data)[0]
		print(rst)
		crawl(rst)
	except Exception as err:
		print(err)

crawl(63579)