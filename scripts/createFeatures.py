import re
import json
f = open('../result/keywordpoint_each_bus')
g = open('../result/subset')
k = open('../result/features','w+')

# Get dict, key is busid, value is keyword,count pairs. i.e. a dict of dict
dic = {}
lines = f.readlines()
for line in lines:
	if re.match('bid',line):
		bid = line.rstrip('\n')
		dic[bid] = {}
		# print bid
	else:
		keyword = line.split('|')[0]
		p = line.split('|')[1]
		n = line.split('|')[2].rstrip('\n')
		if keyword in dic[bid]:
			dic[bid][keyword] = (int(dic[bid][keyword][0])+int(p),int(dic[bid][keyword][1])+int(n))
		else:
			dic[bid][keyword] = (p,n)
# for each in dic:
	# print dic[each]

k.write('bid ')
for i in xrange(200):
	k.write('K' + str(i) +'P K'+str(i) + 'N ')
kl = []
keywords = g.readlines()
for each in keywords:
	kl.append(each.rstrip('\n').split(":")[0])
for each_bid in dic:
	k.write('\n' +each_bid)
	for each_kw in kl:
		for key in dic[each_bid]:
			# print key
			# print each_kw
			if each_kw in key:
				k.write(' ' +str(dic[each_bid][key][0]) + ' ' +str(dic[each_bid][key][1]))
			else:
				k.write(' ' +str(0) + ' ' +str(0))





# for each in kl:
# for i in xrange(len(lines)):
# 	cp = 0
# 	cn = 0
# 	if (re.match('bid', lines[i])):
# 		k.write('\n' + lines[i].split(':')[1])
# 	else:
# 		wl = lines.split('|')
# 		for each in kl:
# 			if each in wl[0]:
# 				cp += wl[1]
# 				cn += wl[2] 
