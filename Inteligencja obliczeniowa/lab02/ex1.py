import pandas as pd
import numpy as np

data = pd.read_csv("iris_with_errors.csv")
data.replace("-", np.nan, inplace=True)

# missing values
print(data.isna().sum())

for row in data.columns:
    if row == "variety":
        continue

    row_median = data[row].median(skipna=True)
    data[row].fillna(row_median, inplace=True)


# missing values
print(data.isna().sum())

data.to_csv("iris_super_duper_clean.csv", index=False)

for row in data.columns:

    if row == "variety":
        continue

    print(data[row])

    print(
        f"All values are in [0; 15] in {row}: ",
        data[row].between(0, 15).all(skipna=True),
    )
