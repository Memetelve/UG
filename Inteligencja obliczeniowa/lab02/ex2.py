import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets  # type: ignore
from sklearn.decomposition import PCA  # type: ignore

iris = datasets.load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)

pcad_iris = PCA(n_components=2).fit(iris.data)
# n_components
print(pcad_iris)
print(pcad_iris.explained_variance_ratio_)
print(pcad_iris.components_)

# calc lost variance
lost_variance = 1 - sum(pcad_iris.explained_variance_ratio_)
print("Lost variance:", lost_variance)

# print(pcad_iris.transform(iris.data))

# plot
for i, target_name in enumerate(iris.target_names):
    plt.scatter(
        pcad_iris.transform(iris.data[iris.target == i, :])[:, 0],
        pcad_iris.transform(iris.data[iris.target == i, :])[:, 1],
        label=target_name,  # label for the legend
    )
plt.legend()
plt.show()
