import re
import sys

f = open("../result/my_reviews")
g = open("../result/cleaned_reviews","w+")
pattern  = re.compile('[:;]+["^-]*[\(\)]+')
lines = f.readlines()

for each in lines:
	if re.match("business_id",each):
		g.write(each)
	elif each =='':
		continue
	elif re.match(r'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*',each):
		g.write('\n')
	elif re.match('business_id',each):
		continue
	else:
		no_space = re.sub(r' +', ' ', each)
		no_emoc = re.sub('[;:][  *\=\-][()O]+','',no_space)
		no_repeated = re.sub(r'[\= \-\!\#\^]+',' ',no_emoc)
		no_dots = re.sub(r'\.+', '.',no_repeated)
		g.write(no_dots.rstrip('\n'))


# f = open("../result/cleaned_reviews")
# g = open("../result/cleaned1_reviews","w+")

###########Below is for dataset 2#########################
# f = open('../result/merged_without_space')
# g = open('../result/cleaned_all_bus_review','w+')
# pattern  = re.compile('[:;]+["^-]*[\(\)]+')
# lines = f.readlines()
# for each in lines:
# 	if re.match('bid',each):
# 		g.write(each)
# 	else:
# 		no_space = re.sub(r' +', ' ', each)
# 		no_emoc = re.sub('[;:][  *\=\-][()O]+','',no_space)
# 		no_repeated = re.sub(r'[\= \-\!\#\^]+',' ',no_emoc)
# 		no_dots = re.sub(r'\.+', '.',no_repeated)
# 		no_special = re.sub(r'\*\^\\+', '' , no_dots)
# 		g.write(no_special)
