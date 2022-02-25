import pandas as pd
import random 
import plotly.express as px
import plotly.figure_factory as ff

data =pd.read_csv("108.csv")
fig = ff.create_distplot([data["Avg Rating"].tolist()],["rating"])
fig.show()