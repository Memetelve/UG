import pandas as pd
from sklearn.model_selection import train_test_split  # type: ignore

DEBUG = True


df = pd.read_csv("iris.csv")

train_set, test_set = train_test_split(df.values, test_size=0.3, random_state=13)


train_set_inputs = train_set[:, 0:4]
train_set_outputs = train_set[:, 4]
test_set_inputs = test_set[:, 0:4]
test_set_outputs = test_set[:, 4]

if DEBUG:
    for i in range(test_set.shape[0]):
        print(sorted(test_set, key=lambda x: x[4])[i])


def classify_iris(sl, sw, pl, pw):
    if sl < 6 and (lambda x: x * 0.9 - 2)(sl) < sw:
        return "setosa"

    elif sl < 6.3 and sw < 3.2:

        return "versicolor"
    return "virginica"


good_predictions = 0

for i in range(test_set.shape[0]):
    if classify_iris(*test_set_inputs[i, :]) == test_set_outputs[i]:
        good_predictions = good_predictions + 1

print(good_predictions)
print(good_predictions / test_set.shape[0] * 100, "%")
