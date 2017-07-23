#encoding:utf-8
'''创建一个从单词到索引的映射'''
import re

WORD_RE = re.compile('\w+')

index = {}

with open("alice.txt",encoding="utf-8") as fp:
	for line_no, line in enumerate(fp,1):
		for match in WORD_RE.finditer(line):
			#将返回的迭代器变成字符串
			word = match.group()
			#列序号
			column_no = match.start()
			#单词位置
			location = (line_no,column_no)
			# #提取单词出现次数
			# occurrences = index.get(word,[])
			# #将单词新出现的位置添加到列表后面
			# occurrences.append(location)
			# #新的列表放回字典中
			# index[word] = occurrences
			index.setdefault(word, []).append(location)

for word in sorted(index,key=str.upper):
	print(word,index[word])
