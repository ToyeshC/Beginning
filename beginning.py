# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import dataset
dataset = pd.read_csv("/Users/toyesh/Documents/Personal/Coding/Data Science/Machine Learning A-Z (Codes and Datasets)/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/R/Data.csv")
x = dataset.iloc[:, :-1].values        # features
y = dataset.iloc[:, -1].values         # dependent variabe

print(x, y, sep = "\n\n")