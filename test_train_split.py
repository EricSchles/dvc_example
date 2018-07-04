import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/data.csv")
X, y = df[["A","B"]], df["C"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

train = pd.concat([X_train, y_train], axis=1)
test = pd.concat([X_test, y_test], axis=1)

train.to_csv("data/train.csv")
test.to_csv("data/test.csv")