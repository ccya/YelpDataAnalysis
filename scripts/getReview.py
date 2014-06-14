import json
from pprint import pprint
myId = 'ikm0UCahtK34LbLCEw4YTw'
f = open('yelp_academic_dataset_review.json')
myReviews = []
bus_ids = []
for line in f:
	data = json.loads(line)
	if data['user_id'] == myId: 
		bus_ids.append(data['business_id'])
		myReviews.append([data['business_id'], data['text']])
f.close()
r = open('my_reviews' , 'wb')
#print(type(myReviews[0]))
for review in myReviews:
	r.write('business_id ' + review[0].encode('utf-8') + '\n')
	r.write(review[1].encode('utf-8') + '\n')
	r.write('************************\n')
	
# f2 = open('yelp_academic_dataset_business.json')
# bus_input = []
# for line in f2:
# 	data = json.loads(line)
# 	bus_input.append(data)
# r2 = open('bus_loc' , 'wb')
# r2.write('business id\n')
# for id in bus_ids:
# 	for bus in bus_input:
# 		if id == bus['business_id']: 
# 			r2.write(id + ' longitude: ' + str(bus['longitude']) + ' latitude: ' + str(bus['latitude']) + ' Category: ' + str(bus['categories']) +'\n')
# 			break

f3 = open('yelp_academic_dataset_review.json')
review_input = []
for line in f3:
	data  = json.loads(line)
	review_input.append(data)
r3 = open('bus_review','w')
r3.write('business id\n')
for id in bus_ids:
	for review in review_input:
		if id == review['business_id']:
			r3.write(id + ' REVIEW: ' + str(review['text'])+ '\n')
		
	
