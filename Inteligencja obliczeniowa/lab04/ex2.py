from sklearn import datasets, model_selection
from sklearn.neural_network import MLPClassifier

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)

# Train a MLP model
mlp = MLPClassifier(hidden_layer_sizes=(2,), max_iter=10000)
mlp.fit(X_train, y_train)

# Evaluate the model
print(mlp.score(X_test, y_test))


mlp = MLPClassifier(hidden_layer_sizes=(3,), max_iter=10000)
mlp.fit(X_train, y_train)

# Evaluate the model
print(mlp.score(X_test, y_test))

mlp = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=10000)
mlp.fit(X_train, y_train)

# Evaluate the model
print(mlp.score(X_test, y_test))
