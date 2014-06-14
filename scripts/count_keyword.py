import operator
f = open('../result/keywords')
g = open('../result/sorted_keywords','w+')
lines = f.readlines()
dic = {}
for each in lines:
	# print each
	if each in dic:
		dic[each] = dic[each]+1
	else:
		dic[each] = 1
sdic = sorted(dic.iteritems(), key=operator.itemgetter(1),reverse = True)
# print type(sdic)
for each in sdic:
	word = each[0].split(',')[0].rstrip('\n')
	time = each[1]
	g.write(word + ":" + str(time)+'\n')
