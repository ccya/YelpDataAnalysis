import random
import re
f = open('../result/cleaned_all_bus_review')
g = open('../result/label.rtf')
all_bus_id = []
my_id = []
my_id_label = {}

k = open('../result/all_bus_id','w+')
lines = f.readlines()
for each in lines:
	if re.match('bid',each):
		bid = each[4:]
		all_bus_id.append(bid.rstrip('\n'))

myreviewbus = g.readlines()
for each in myreviewbus:
	bid = each.split(' ')[1]
	my_id.append(bid)
	label = each.split(' ')[2].rstrip('\n')
	# print bid
	# print label[0]
	my_id_label[bid] = label[0]

for each in my_id:
	if each in all_bus_id:
		all_bus_id.remove(each)
for each in all_bus_id:
	k.write(each + '\n')


h = open('../result/sampled_bid','w+')
m = open('../result/not_sampled_bid','w+')


new_my_id = list(set(my_id))
my_count = len(new_my_id)
# total_count = len(all_bus_id)
x = int(2*my_count/3)

sample = random.sample(new_my_id, x)

# print len(new_my_id)

for each in new_my_id:
	if each in sample:
		# c+=1
		h.write(each +": " + my_id_label[each] +'\n')
	else:
		m.write(each +": " + my_id_label[each] +'\n')
