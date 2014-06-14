import json
f = open('../data/yelp_academic_dataset_review.json')
reviews = []
count = 0
lastId = ''
review_counts = []
for line in f:
	data = json.loads(line)
	reviews.append(data)
	
sorted_reviews = sorted(reviews, key=lambda x: x['business_id'])
r = open('../result/sorted_reviews_bid' , 'wb')
for review in sorted_reviews:
	r.write(bytes(json.dumps(review) + '\n', 'utf-8'))
	if review['business_id'] == lastId:
		count += 1
	else:
		review_counts.append([lastId, count])
		lastId = review['business_id']
		count = 1
review_counts.append([lastId, count])
review_counts.sort(key=lambda x: x[1], reverse=True)
print(review_counts[0])
print(review_counts[1])
r2 = open('../result/count_reviews_bid' , 'wb')
for data in review_counts:
	r2.write(bytes(data[0] + ': ' + str(data[1]) + '\n', 'utf-8'))