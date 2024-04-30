import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets  # type: ignore
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

iris = datasets.load_iris()

X = iris.data

# Create a scatter plot with color and legend
for i in range(3):
    plt.scatter(
        X[iris.target == i, 0],
        X[iris.target == i, 1],
        label=iris.target_names[i],
    )

plt.legend()
plt.show()

print("Before scaling:")
print("Min:", np.min(X, axis=0))
print("Max:", np.max(X, axis=0))
print("Mean:", np.mean(X, axis=0))
print("Standard deviation:", np.std(X, axis=0))


minmax_scaler = MinMaxScaler()
X_scaled = minmax_scaler.fit_transform(X)

for i in range(3):
    plt.scatter(
        X[iris.target == i, 0],
        X[iris.target == i, 1],
        label=iris.target_names[i],
    )

plt.legend()
plt.show()

print("After min max scaling:")
print("Min:", np.min(X_scaled, axis=0))
print("Max:", np.max(X_scaled, axis=0))
print("Mean:", np.mean(X_scaled, axis=0))
print("Standard deviation:", np.std(X_scaled, axis=0))

zscore_scaler = StandardScaler()
X_scaled = zscore_scaler.fit_transform(X)

for i in range(3):
    plt.scatter(
        X[iris.target == i, 0],
        X[iris.target == i, 1],
        label=iris.target_names[i],
    )

plt.legend()
plt.show()

print("After z-score scaling:")
print("Min:", np.min(X_scaled, axis=0))
print("Max:", np.max(X_scaled, axis=0))
print("Mean:", np.mean(X_scaled, axis=0))
print("Standard deviation:", np.std(X_scaled, axis=0))


# In min-max scaling, the data is scaled to a fixed range between 0 and 1. In z-score scaling, the data is scaled so that it has a mean of 0 and a standard deviation of 1, often called standardization.
