import re
import sys


################################################################################
#------------------Find keyword for all review of ONE usr-----------------------
f = open('../result/chunck')
g = open('../result/keywords','w+')
k = open('../result/adj_keyword','w+')
keywords_adj = {}
lines = f.readlines()
ladj = []

for i in xrange(len(lines)):
	if re.match("business_id", lines[i]):
		k.write(lines[i])
	if re.match("  \(NP",lines[i]):
		keyword = re.sub(r'NP|/NNP|/NNS|/NN|[()]|', '',lines[i]).rstrip('\n')[3:]
		if len(keyword)!=0:
			# g.write(keyword+'\n')
			k.write(keyword + ":")
			j = i+1
			find = True
			ladj = []
			while(find):
				if len(lines[j])<4:
					if j == len(lines) - 1:
						find = False
					else:
						j = j+1
				else:
					if re.search(r'\/JJ',lines[j][-4:]) is not None:
						adj = re.sub(r'/JJ|/JJS|/JJR','',lines[j]).rstrip('\n')[2:]
						ladj.append(adj)
						if keyword in keywords_adj:
							keywords_adj[keyword].append(adj)
						else:
							keywords_adj.setdefault(keyword,[adj])
						j = j+1
					elif re.match("  \(NP",lines[j]):
						find = False
						k.write(",".join(ladj)+ " \n")
					elif j == len(lines)-1:
						find = False
						k.write(",".join(ladj)+ " \n")
					elif re.match('business_id',lines[j]):
						find = False
						k.write(",".join(ladj)+ " \n")
					else:
						j = j+1
for each in keywords_adj:
	g.write(each + ':' + (',').join(keywords_adj[each])+ '\n')
################################################################################


################################################################################
#------------------Find keyword for all review of ONE usr-----------------------
# f = open('../result/chunck_allbus')
# g = open('../result/keywords_each_bus','w+')
# k = open('../result/adj_keyword_each_bus','w+')
# adj = []
# lines = f.readlines()
# for i in xrange(len(lines)):
# 	if re.match('bid',lines[i]):
# 		g.write('\n'+lines[i])
# 		k.write(lines[i])
# 	elif re.match("  \(NP",lines[i]):
# 		keyword = re.sub(r'NP|/NNP|/NNS|/NN|[()]|', '',lines[i]).rstrip('\n')[3:]
# 		if len(keyword)!=0:
# 			g.write(keyword+'|')
# 			k.write(keyword+':')
# 			j = i+1
# 			find = True
# 			while(find):
# 				if len(lines[j])<4:
# 					j = j+1
# 				else:
# 					if re.search(r'\/JJ',lines[j][-4:]) is not None:
# 						wadj = re.sub(r'/JJ|/JJS|/JJR','',lines[j]).rstrip('\n')[2:]
# 						adj.append(wadj)
# 						# else:
# 							# keywords_adj.setdefault(keyword,[adj])
# 						j = j+1
# 					elif re.match("  \(NP",lines[j]):
# 						find = False
# 						k.write('|'.join(adj)+'\n')
# 						adj = []
# 					elif j == len(lines)-1:
# 						find = False
# 						k.write('|'.join(adj)+'\n')
# 						adj = []
# 					else:
# 						j = j+1
# for each in keywords_adj:
	# k.write(each + ':' + (',').join(keywords_adj[each])+ '\n')
################################################################################
