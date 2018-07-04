import pandas as pd
import random

df = pd.DataFrame()

for _ in range(1000):
    tmp = {
        "A": random.random(),
        "B": random.random(),
        "C": random.randint(0, 10)
    }
    df = df.append(tmp, ignore_index=True)

df.to_csv("data/data.csv")