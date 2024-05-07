import apyori
import pandas as pd
import numpy as np


data = pd.read_csv("titanic.csv", header=None)

print(len(data.values) - 1)

items = [
    [data.values[i + 1, j + 1] for j in range(len(data.values[0]) - 1)]
    for i in range(len(data.values) - 1)
]

# print(items)

association_rules = apyori.apriori(
    items, min_support=0.05, min_confidence=0.8, min_lift=1.2
)

association_rules: list[apyori.RelationRecord] = sorted(
    association_rules, key=lambda x: x[2][0][2], reverse=True
)


for rule in association_rules:

    if len(rule.items) == 0:
        continue

    if all(x not in rule.items for x in ["No", "Yes"]):
        continue

    for subset in rule.ordered_statistics:

        print(
            subset.items_base,
            "=>",
            subset.items_add,
            "conf:",
            subset.confidence,
            "supp:",
            rule.support,
            "lift:",
            subset.lift,
        )

    # print(rule.ordered_statistics[0].items_base)

    # print(rule)
    # print("\n")
