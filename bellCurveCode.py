
import plotly.figure_factory as ff

import pandas as pd

import csv






df = pd.read_csv("data.csv")  # you can change this value to whatever the data file's name is(if it is not showing output, it might be because data file is not same name)

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])


fig.show()
