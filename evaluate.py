import pickle
import pandas as pd
from sklearn.metrics import r2_score

with open("model.p", "rb") as model_file:
    lin_reg = pickle.load(model_file)

test = pd.read_csv("data/test.csv")

predicted = lin_reg.predict(test[["A","B"]])

score = r2_score(test["C"], predicted)

with open("metrics.txt", "w") as metrics:
    metrics.write("r^2: {}".format(score)) 
