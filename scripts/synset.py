#encoding:utf-8
from nltk.corpus import wordnet as wn

# p = open('../result/ori_pos')
p = open('../result/positive-words.txt')
poswords = p.readlines()
n = open('../result/negative-words.txt')
# n = open('../result/ori_neg')
negwords = n.readlines()

pos_list = []
neg_list = []

for each in poswords:
	pos_list.append(each.rstrip('\n'))
for each in negwords:
	neg_list.append(each.rstrip('\n'))

pos = []
neg = []
# for positive words. get their synonyms and antonyms
for each in pos_list:
	synonyms = wn.synsets(each,pos=wn.ADJ) 
	for eachsyn in synonyms:
		for pword in eachsyn.lemma_names:
			pos.append(pword)
		if len(eachsyn.lemmas[0].antonyms())!=0:
			for lemma in eachsyn.lemmas[0].antonyms():
				nword = lemma.name
				neg.append(nword)

# for negative words. get their synonyms and antonyms
for each in neg_list:
	synonyms = wn.synsets(each,pos = wn.ADJ)
	for eachsyn in synonyms:
		for pword in eachsyn.lemma_names:
			neg.append(pword)
		if len(eachsyn.lemmas[0].antonyms())!=0:
			for lemma in eachsyn.lemmas[0].antonyms():
				nword = lemma.name
				pos.append(nword)
final_pos =  list(set(pos + pos_list)) 
final_neg = list(set(neg + neg_list))
print len(final_pos)
print len(final_neg)
# print final_pos
# f = open('../result/pos','w+')
# g = open('../result/neg','w+')

f = open('../result/pos_all','w+')
g = open('../result/neg_all','w+')
for each in final_pos:
	f.write(each + '\n')
for each in final_neg:
	g.write(each + '\n')


