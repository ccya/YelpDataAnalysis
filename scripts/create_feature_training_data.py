import re
import json
f = open('../result/keywordpoint_train')
g = open('../result/subset')
# h = open('../result/sampled_bid')
h = open('../result/not_sampled_bid')
m = open('../result/loc_feature')
# k = open('../result/features_train','w+')
k = open('../result/features_dev','w+')

#Get labels
bids = h.readlines()
bidlist = []
labels = {}
for each in bids:
	bid = each.split(':')[0]
	label = each.split(':')[1].rstrip('\n')
	labels[bid] = label
	bidlist.append(bid)

# Get loc features
loc_fea = {}
locinfo = m.readlines()
for each in locinfo:
	bid = each.split(' ')[0]
	fear = each.split(' ')[1].rstrip('\n')
	loc_fea[bid] = fear


# Get dict, key is busid, value is keyword,count pairs. i.e. a dict of dict
dic = {}
put = False
lines = f.readlines()
for line in lines:
	if re.match('business_id',line):
		bid = line.split(" ")[1].rstrip('\n')
		if bid in bidlist:
		# if bid not in bidlist:
			dic[bid] = {}
			put = True
		else:
			put = False
	else:
		keyword = line.split('|')[0]
		p = line.split('|')[1]
		n = line.split('|')[2].rstrip('\n')
		if put:
			if keyword in dic[bid]:
				dic[bid][keyword] = (int(dic[bid][keyword][0])+int(p),int(dic[bid][keyword][1])+int(n))
			else:
				dic[bid][keyword] = (p,n)

#Start to create feature

k.write('label loc ')
for i in xrange(200):
	k.write('K' + str(i) +'P K'+str(i) + 'N ')
kl = []
keywords = g.readlines()
for each in keywords:
	kl.append(each.rstrip('\n').split(":")[0])

for each_bid in dic:
	k.write('\n' +labels[each_bid])
	# Y.append(labels[each_bid])
	k.write('|' + loc_fea[each_bid])
	instance = [loc_fea[each_bid]]
	for each_kw in kl:
		found = False
		for key in dic[each_bid]:
			if key in each_kw:
				value = '|' +str(dic[each_bid][key][0]) + '|' +str(dic[each_bid][key][1])
				k.write(value)
				# instance.append('|')
				# instance.append(str(dic[each_bid][key][0]))
				# instance.append('|')
				# instance.append(str(dic[each_bid][key][1]))
				found = True
				break
		if not found:
			value = '|' +str(0) + '|' +str(0)
			k.write(value)
			# instance.append('|')
			# instance.append(str(0))
			# instance.append('|')
			# instance.append(str(0))
	# print len(instance)

	# for each_kw in kl:
	# 	for key in dic[each_bid]:
	# 		# print key
	# 		# print each_kw
	# 		if each_kw in key:
	# 			k.write('|' +str(dic[each_bid][key][0]) + '|' +str(dic[each_bid][key][1]))
	# 		else:
	# 			k.write('|' +str(0) + '|' +str(0))





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
