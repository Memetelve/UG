from sklearn import model_selection
from sklearn.neural_network import MLPClassifier
import pandas as pd

# read diabetes data
data = pd.read_csv("diabetes 1.csv")

# split data into features and target
X = data.drop(columns=["class"])
y = data["class"]

# split data into training and test sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)

# train a MLP model
mlp = MLPClassifier(hidden_layer_sizes=(6, 3), max_iter=500)
mlp.fit(X_train, y_train)

# evaluate the model
print(mlp.score(X_test, y_test))


# FN gorsze ponieważ ktoś może dalej żyć bez wiedzy, a jak zdarzy się FP to pradowpodobnie bedzie wiecej badan
