import pickle

pickle_file = open("banner.p","rb")
rst = pickle.load(pickle_file)
for line in rst:
 	print(''.join(map(lambda x: x[0]* x[1], line)))