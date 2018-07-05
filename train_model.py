from sklearn import linear_model
import pandas as pd
import pickle

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

lin_reg = linear_model.Lasso(alpha=0.1)
lin_reg.fit(train[["A", "B"]], train["C"])

with open("model.p", "wb") as output_file:
    pickle.dump(lin_reg, output_file)
