import json
f = open('yelp_academic_dataset_review.json')
reviews = []
count = 0
lastId = ''
review_counts = []
for line in f:
	data = json.loads(line)
	reviews.append(data)
	
sorted_reviews = sorted(reviews, key=lambda x: x['user_id'])
r = open('sorted_reviews' , 'wb')
for review in sorted_reviews:
	r.write(bytes(json.dumps(review) + '\n', 'utf-8'))
	if review['user_id'] == lastId:
		count += 1
	else:
		review_counts.append([lastId, count])
		lastId = review['user_id']
		count = 1
review_counts.append([lastId, count])
review_counts.sort(key=lambda x: x[1], reverse=True)
print(review_counts[0])
print(review_counts[1])
r2 = open('count_reviews' , 'wb')
for data in review_counts:
	r2.write(bytes(data[0] + ': ' + str(data[1]) + '\n', 'utf-8'))