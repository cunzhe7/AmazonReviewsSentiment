import numpy as np
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV
from scipy import stats


kf = KFold(n_splits = 5,shuffle = True)


# param_dist = {"C": stats.uniform(2,10),
#               "gamma": stats.uniform(0.1,5),
#               "degree": stats.randint(2,6),
#               "kernel": ["linear", "poly","rbf","sigmoid"]}


# rands = RandomizedSearchCV(SVC(),param_distributions = param_dist, n_iter = 100,cv = kf)


train_X = np.loadtxt("text.txt", delimiter = ',')
# print(train_X.shape)
# print(train_X)
# train_X = train_X.reshape(9252,2)
# print(train_X.shape)
# print(train_X)
train_Y = np.loadtxt("rate.txt")
# print(train_Y.shape)
train_Y = train_Y.reshape(9252,1)

# print(train_Y==0)
# newXN = np.where(train_Y==0,train_X)
# print(newXN.shape)
# newXP = train_X[train_Y==1]
# print(newXP.shape)
# # np.full()

newXN = train_X[0:1400,:]
newXP = train_X[4000:5400,:]
newYN = train_Y[0:1400,:]
newYP = train_Y[0:1400,:]

newX = np.concatenate((newXN,newXP),axis = 0)
newY = np.concatenate((newYN,newYP),axis = 0)
print(newX.shape)
print(newY.shape)




test_X  = np.loadtxt("test.txt", delimiter = ',')
test_Y = np.loadtxt("testrate.txt")
test_Y = test_Y.reshape(23009,1)

# rands.fit(train_X,train_Y.ravel())
# print("Tuned paramaters: {}".format(rands.best_params_))



# acc = 0
# for train_index, test_index in kf.split(newX):
#     X_train, X_test = newX[train_index], newX[test_index]
#     Y_train, Y_test = newY[train_index], newY[test_index]
#     clf = SVC(C = 4.67702170675376, kernel = 'rbf', degree = 3, gamma = 5)
#     clf.fit(X_train,Y_train.ravel())
#     prediction = clf.predict(X_test)
    
#     # print(*prediction)
#     acc = acc + accuracy_score(Y_test, prediction)

# print(acc/5)



clf = SVC(C = 4.67702170675376, kernel = 'rbf', degree = 3, gamma = 5)
clf.fit(newX,newY.ravel())

prediction = clf.predict(test_X)

print(accuracy_score(test_Y,prediction))

