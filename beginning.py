# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import dataset
dataset = pd.read_csv("/Users/toyesh/Documents/Personal/Coding/Python/Data.csv")
x = dataset.iloc[:, :-1].values        # features
y = dataset.iloc[:, -1].values         # dependent variable

# missing data handling
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, 1:3])

x[:, 1:3] = imputer.transform(x[:, 1:3])

print(x)