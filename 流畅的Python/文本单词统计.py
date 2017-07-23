import re

count = 0
WORD_RE = re.compile("\w+")

with open("alice.txt",encoding="utf-8") as fp:
	for _,line in enumerate(fp):
		for match in WORD_RE.finditer(line):
			word = match.group()
			count += 1
print(count)