import pandas as pd
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

USELESS_PRINTS = True


df = pd.read_csv("iris.csv")

train_set, test_set = train_test_split(df.values, test_size=0.3)


train_set_inputs = train_set[:, 0:4]
train_set_outputs = train_set[:, 4]
test_set_inputs = test_set[:, 0:4]
test_set_outputs = test_set[:, 4]

for k in [3, 5, 11]:
    knn = KNeighborsClassifier(n_neighbors=k)
    classifier = knn.fit(train_set_inputs, train_set_outputs)

    score = classifier.score(test_set_inputs, test_set_outputs)
    print(f"Score for k={k}: {score * 100:.2f}%")

    if USELESS_PRINTS:
        predictions = classifier.predict(test_set_inputs)
        conf_matrix = confusion_matrix(test_set_outputs, predictions)
        print(conf_matrix)

gnb = GaussianNB()
classifier = gnb.fit(train_set_inputs, train_set_outputs)
score = classifier.score(test_set_inputs, test_set_outputs)
print(f"Score for GaussianNB: {score * 100:.2f}%")

if USELESS_PRINTS:
    predictions = classifier.predict(test_set_inputs)
    conf_matrix = confusion_matrix(test_set_outputs, predictions)
    print(conf_matrix)

scores = [[0, None] for _ in range(5)]

n = 1000
for _ in range(n):
    train_set, test_set = train_test_split(df.values, test_size=0.3)

    train_set_inputs = train_set[:, 0:4]
    train_set_outputs = train_set[:, 4]
    test_set_inputs = test_set[:, 0:4]
    test_set_outputs = test_set[:, 4]

    for i, model in enumerate(
        [
            DecisionTreeClassifier(),
            KNeighborsClassifier(n_neighbors=3),
            KNeighborsClassifier(n_neighbors=5),
            KNeighborsClassifier(n_neighbors=11),
            GaussianNB(),
        ]
    ):
        classifier = model.fit(train_set_inputs, train_set_outputs)
        score = classifier.score(test_set_inputs, test_set_outputs)
        scores[i][0] = scores[i][0] + score

        if scores[i][1] is None:
            scores[i][1] = (
                classifier.__class__.__name__ + (f" (k={classifier.n_neighbors})")
                if hasattr(classifier, "n_neighbors")
                else classifier.__class__.__name__
            )


print("Average scores:")
for score, model in sorted(scores, key=lambda x: x[0]):
    print(f"{model}: {score / n * 100:.2f}%")
