import json
import math
import collections
f = open('../result/bus_loc')
g = open('../data/yelp_academic_dataset_business.json')
k = open('../result/loc_feature','w+')
loc = {}
alldist = []
lines = f.readlines()
latitude = 0
longtitude = 0
for each in lines:
	longtitude += float(each.split(":")[1].split(" ")[1])
	latitude += float(each.split(":")[2].split(" ")[1])
center_lat = latitude/774
center_long = longtitude/774

max = 0.0
preferd = []
for each in lines:
	lon = float(each.split(":")[1].split(" ")[1])
	lat = float(each.split(":")[2].split(" ")[1])
	dist = math.sqrt((lat - center_lat)**2 + (lon - center_long)**2)
	preferd.append(dist)
sorted_preferd = sorted(preferd)

length = len(sorted_preferd)
medium_1 = 0.0
if not length % 2:
	medium_1 = (sorted_preferd[length/2]+sorted_preferd[length/2-1])/2.0
else:
	medium_1 = sorted_preferd[length/2]
print medium_1


for line in g:
	data = json.loads(line)
	lat = data["latitude"]
	lon = data["longitude"]
	dist = math.sqrt((lat - center_lat)**2 + (lon - center_long)**2)
	alldist.append(dist)
	loc[data["business_id"]] = dist

sorted_dist = sorted(alldist)

# length = len(sorted_dist)
# medium = 0.0
# if not length % 2:
# 	medium = (sorted_dist[length/2]+sorted_dist[length/2-1])/2.0
# else:
# 	medium = sorted_dist[length/2]
# print medium

fea_loc = {}
for each in loc:
	if loc[each]<medium_1:
		fea_loc[each] = 0
	else:
		fea_loc[each] = 1
result = collections.OrderedDict(sorted(fea_loc.items()))
for each in result:
	k.write(each+ " " + str(fea_loc[each])+"\n")