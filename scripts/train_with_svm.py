from sklearn import svm
f = open('../result/features_train')
g = open('../result/features_dev')
lines = f.readlines()
dev_lines = g.readlines()
Y = []
X = []
X_dev = []
Y_dev = []
for each in lines[1:]:
	wl = each.split('|')
	instance = []
	for i in xrange(len(wl)):
		if i == 0:
			label = wl[i][1]
			Y.append(label)
		else:
			instance.append(wl[i].rstrip('\n'))
	# print wl[1]
	# Y.append(wl[0][1])
	# instance.append(wl[1])
	X.append(instance)
clf = svm.SVC()
clf.fit(X,Y)

for each in dev_lines[1:]:
	wl = each.split('|')
	instance = []
	for i in xrange(len(wl)):
		if i == 0:
			label = wl[i][1]
			Y_dev.append(label)
		else:
			instance.append(wl[i].rstrip('\n'))
	# print len(instance)
	# Y_dev.append(wl[0][1])
	# instance.append(wl[1])
	X_dev.append(instance)
result = clf.predict(X_dev)
right = 0
# print Y_dev[3]
# print result[2]
# print result
right = 0
for i in xrange(len(result)):
	# print str(Y_dev[i]) + str(result[i])
	if result[i] == Y_dev[i]:
		right += 1
		# print right
print right
print len(result)
# print float(right/len(result))
