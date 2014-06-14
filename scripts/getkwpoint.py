import re
f = open('../result/pos')
g = open('../result/neg')
k = open('../result/adj_keyword')
r = open('../result/keywordpoint_train','w+')
# f = open('../result/pos_all')
# g = open('../result/neg_all')
# k = open('../result/adj_keyword_each_bus')
# r = open('../result/keywordpoint_each_bus','w+')
pairs = k.readlines()
pos = f.readlines()
neg = g.readlines()
posword = []
negword = []
for line in pos:
	posword.append(line.rstrip('\n'))
for line in neg:
	negword.append(line.rstrip('\n'))

for pair in pairs:
	if(re.match('business_id',pair)):
		r.write(pair)
	else:
		p = 0
		n = 0
		wl = pair.split(':')
		keyword = wl[0]
		if len(wl) != 0:
			adjl = wl[1].split(',')
			for adj in adjl:
				nadj = adj.rstrip('.').rstrip('\n')
					# print nadj
				if nadj in posword:
					p +=1
				elif nadj in negword:
					n +=1
			value = keyword + "|" + str(p) +  "|" +str(n)
			r.write(value+'\n')
		else:
			value = keyword + "|" + str(0) +  "|" +str(0)
			r.write(value+'\n')
#############################Dataset 2###################
# for pair in pairs:
# 	if(re.match('bid',pair)):
# 		r.write(pair)
# 	else:
# 		p = 0
# 		n = 0
# 		wl = pair.split(':')
# 		keyword = wl[0]
# 		adjl = wl[1].split('|')
# 		for adj in adjl:
# 			nadj = adj.rstrip('.').rstrip('\n')
# 			# print nadj
# 			if nadj in posword:
# 				p +=1
# 			elif nadj in negword:
# 				n +=1
# 		value = keyword + "|" + str(p) +  "|" +str(n)
# 		r.write(value + '\n')
	# print value


