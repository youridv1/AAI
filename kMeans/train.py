import kMeans as km

dataset = km.genDataSet("dataset1.csv")
labels = km.genLabels("dataset1.csv", 2000)
scalers = km.findminmax(dataset)
scaleddata = km.scale(dataset, scalers)

results = []
tmp = 0
for k in range(2, 50):
    results = []
    for _ in range(10):
        clusters, _, _ = km.kMeans(scaleddata, k, labels)
        total = 0
        for l in clusters:
            for m in l:
                total += m[0]
        results.append(total)
    tmp = min(results)
    print(k, tmp / k)
