import math
import csv
import plotly.express as px
import pandas as pd

df = pd.read_csv('class1.csv')
fig = px.scatter(df, x='Student Number', y='Marks', title='Revision')
fig.show()