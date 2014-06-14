import nltk
import sys
import re
####################################################################
# This below is for token and tag to get keywords of usr review data
# ------------------------------------------------------------------
f = open('../result/cleaned_reviews')
g = open('../result/token_tagged','w+')
h = open('../result/chunck','w+')
lines =f.readlines()
newreview = ''
grammer = "NP: {<N.*>+}"
cp = nltk.RegexpParser(grammer)
for each in lines:
	if re.match("business_id",each):
		g.write(each)
		h.write(each)
	else:
		tagged = []
		sentences = nltk.sent_tokenize(each)
		for sent in sentences:
			newsent = nltk.word_tokenize(sent)
			result = nltk.pos_tag(newsent)
			tagged = tagged + result
		result = cp.parse(tagged)
		g.write(str(tagged)+'\n')
		h.write(str(result)+'\n')
# ------------------------------------------------------------------
####################################################################


####################################################################
# This below is for token and tag for all bus review data to get keywords for each bid
# ------------------------------------------------------------------
# f = open('../result/cleaned_all_bus_review_2')
# g = open('../result/token_tagged_allbus_2','w+')
# h = open('../result/chunck_allbus_2','w+')
# lines =f.readlines()
# newreview = ''
# grammer = "NP: {<N.*>+}"
# cp = nltk.RegexpParser(grammer)
# for each in lines:
	# if re.match('bid',each):
		# g.write(each)
		# h.write(each)
	# else:
		##tagged = []
		##sentences = nltk.sent_tokenize(each.rstrip('\n'))
		##for sent in sentences:
		# newsent = nltk.word_tokenize(each.rstrip('\n'))
		# tagged = nltk.pos_tag(newsent)
		##tagged = tagged + result
		# result = cp.parse(tagged)
		# g.write(str(tagged)+'\n')
		# h.write(str(result)+'\n')
# ------------------------------------------------------------------
####################################################################