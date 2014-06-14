import json
f = open('../result/sorted_reviews_bid')
reviews = []
count = 0
lastId = '--4Pe8BZ6gj57VFL5mUE8g'
review_counts = []
g = open('../result/merged_review_bid','w+')
# print len(f.readlines())
for line in f:
	data = json.loads(line)
	if data['business_id'] == lastId:
		count +=1
		reviews.append(data['text'])
	else:
		merged_review = '.'.join(reviews)
		g.write(('bid: ' + lastId + '\n' + merged_review).encode('utf-8') + '\n')
		merged_review = ''
		lastId = data['business_id']
