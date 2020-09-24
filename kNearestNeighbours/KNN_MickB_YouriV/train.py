# Vindt de optimale K met behulp van de validatieset en beantwoordt de vraag met deze K.
from kNN import findK, scale, genDataSet, genLabels, findLabel, findminmax, scale2

#generate dataset and validationset
data = genDataSet("dataset1.csv")

scalers = findminmax(data)
weights = [1, 1, 2, 4, 2, 1, 3]

scaleddata = scale2(data, scalers, weights)
scaledvaliddata = scale2(genDataSet("validation1.csv"), scalers, weights)
scaledtestdata = scale2(genDataSet("days.csv"), scalers, weights)

#generate labels for aformentioned sets
labels = genLabels("dataset1.csv", 2000)
validlabels = genLabels("validation1.csv", 2001)

# #find optimal K value and corresponding accuracy
# accuracy, optimalK = findK(scaleddata, scaledvaliddata, labels, validlabels)

# # generate and print labels for testdata
# print(findLabel(scaleddata, scaledtestdata, labels, optimalK))
# print("Used K: ", optimalK)
# print("Accuracy validationset: ", accuracy)

# Beantwoordt de vraag voor onze top 5 K's.
optimalKs = [52, 53, 58]
for currentK in optimalKs:
    print(findLabel(scaleddata, scaledtestdata, labels, currentK))
    print("Used K: ", currentK)