from sklearn import model_selection
from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.metrics import confusion_matrix


# read diabetes data
data = pd.read_csv("diabetes 1.csv")

# split data into features and target
X = data.drop(columns=["class"])
y = data["class"]


# print(X)
# print(y)

# split data into training and test sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X, y, test_size=0.3, random_state=1
)

# train a MLP model
mlp = MLPClassifier(activation="tanh", hidden_layer_sizes=(5, 9), max_iter=500)
mlp.fit(X_train, y_train)

# evaluate the model
print(mlp.score(X_test, y_test))

print("confusion matrix:")
print(confusion_matrix(y_test, mlp.predict(X_test)))


# FN gorsze ponieważ ktoś może dalej żyć bez wiedzy, że jest chory, a jak zdarzy się FP to pradowpodobnie bedzie wiecej badan
