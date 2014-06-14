import operator
# f = open('../result/sorted_keywords')
g = open('../result/keywordpoint')
points = g.readlines()
# put the points for keywords in dictionary
point_dic = {}
weight_dic = {}
for each in points:
	pairs = each.rstrip('\n').split('|')
	keyword  = pairs[0]
	weight =  pairs[1] + pairs[2]
	point_dic.setdefault(keyword, (pairs[1],pairs[2]))
	weight_dic.setdefault(keyword, weight)
sorted_weight_dic = sorted(weight_dic.iteritems(), key=operator.itemgetter(1),reverse = True)
# print sorted_weight_dic[0]
# set the subset size
size = 200
# get the subset keywords and corresponding point
result = {}
for i in xrange(size):
	word = sorted_weight_dic[i][0]
	if word in point_dic:
		point = point_dic[word]
		# print point
		result.setdefault(word,point)
	else:
		result.setdefault(word,(0,0))
k = open('../result/subset','w+')
for each in result:
	value = each + ":" + str(result[each])
	k.write(value + '\n')