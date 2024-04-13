import pandas as pd
from sklearn.model_selection import train_test_split  # type: ignore

df = pd.read_csv("iris.csv")

print(df.head())

train_set, test_set = train_test_split(df, test_size=0.3, random_state=13)

print(test_set)
print(test_set.shape[0])

train_set_inputs = train_set[:, :4]
train_set_outputs = train_set[:, 4]
test_set_inputs = test_set[:, :4]
test_set_outputs = test_set[:, 4]
