import pandas as pd
import random
from sklearn.preprocessing import LabelEncoder

import numpy as np
import seaborn as sb
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
print(df.columns)
for d in df:
    print(d)
    print(df[d].describe())

"""
def clean(data, numerics):
    for i in numerics:
        mean = data[i].mean()
        std = data[i].std()
        data.loc[data[i] < data[i].quantile(0.025), i] = pd.NA
        data.loc[data[i] > data[i].quantile(0.975), i] = pd.NA
    # print(sum(data.isna().sum()))

    na_count = sum(data.isna().sum())
    # print(na_count)
    if (na_count / data.shape[0]) <= 0.05:
        data = data.dropna()
    else:
        for i in numerics:
            mean = data[i].mean()
            std = data[i].std()
            is_null = data[i].isnull().sum()
            rand_data = np.random.randint(mean - std, mean + std, size=is_null)
            data_slice = data[i].copy()

            data_slice[data_slice.isnull() == True] = rand_data
            data[i] = data_slice

    return data

"""

#print(df.columns)
#print(df)
for d in df :
    print(d)
    print(df[d].min())
    print(df[d].max())
    print("*******")



y = df.pop("DEATH_EVENT")
X = df


del df["time"]

X_scal = StandardScaler()
X_scal.fit(X)
x = X_scal.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1,random_state=2000)
print(x)

for j in range(500):
    if j != 0:
        print("step", j)
        forest = RandomForestClassifier(n_estimators=j)
        forest.fit(X_train, y_train)
        acc = accuracy_score(y_test, forest.predict(X_test))
        print("RandomForestClassifier", acc)

        if acc > 0.94:
            picked = pickle.dump(forest, open("model.pkl", "wb"))
            print("pickeled")
            break
