import pandas as pd
from sklearn.model_selection import train_test_split  # type: ignore
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import confusion_matrix

DEBUG = False
USELESS_PRINTS = True


df = pd.read_csv("iris.csv")

train_set, test_set = train_test_split(df.values, test_size=0.3)

if USELESS_PRINTS:
    print(train_set)
    print(test_set)

train_set_inputs = train_set[:, 0:4]
train_set_outputs = train_set[:, 4]
test_set_inputs = test_set[:, 0:4]
test_set_outputs = test_set[:, 4]


decision_tree = DecisionTreeClassifier()
classifier = decision_tree.fit(train_set_inputs, train_set_outputs)

if USELESS_PRINTS:
    # print classifier in text format
    print(export_text(classifier))
    plt.figure(figsize=(15, 10))
    plot_tree(
        classifier, filled=True, feature_names=list(df.columns[:4]), class_names=True
    )
    plt.show()

score = classifier.score(test_set_inputs, test_set_outputs)
print(f"Score: {score * 100:.2f}%")

if USELESS_PRINTS:
    predictions = classifier.predict(test_set_inputs)
    conf_matrix = confusion_matrix(test_set_outputs, predictions)
    print(conf_matrix)
