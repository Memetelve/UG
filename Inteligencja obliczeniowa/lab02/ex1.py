import pandas as pd
import numpy as np

from difflib import SequenceMatcher

possible_names = ["Setosa", "Versicolor", "Virginica"]


def fix_name(name: str) -> str:
    if name in possible_names:
        return name

    return max(
        possible_names,
        key=lambda x: SequenceMatcher(None, x, name).ratio(),
    )


data = pd.read_csv("iris_with_errors.csv")
data.replace("-", np.nan, inplace=True)


# missing values
print(data.isna().sum())

for row in data.columns:
    if row == "variety":
        data[row] = data[row].apply(fix_name)
        continue

    data[row] = data[row].apply(pd.to_numeric, errors="coerce")

    row_median = data[row].median(skipna=True)
    data[row].fillna(row_median, inplace=True)
    data[row] = data[row].apply(lambda x: row_median if x <= 0 or x > 15 else x)


# missing values
print(data.isna().sum())

data.to_csv("iris_super_duper_clean.csv", index=False)
