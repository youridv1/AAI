# Beantwoordt de vraag met gegeven K
from kNN import findK, scale, genDataSet, genLabels, findLabel

#generate dataset
scaleddata = scale(genDataSet("dataset1.csv"))
#generate validationset
scaledtestdata = scale(genDataSet("days.csv"))

#generate list of labels for dataset
labels = genLabels("dataset1.csv", 2000)

#generate and print labels for testdata
print(findLabel(scaleddata, scaledtestdata, labels, 61))