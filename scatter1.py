import csv
import plotly.express as px
import pandas as pd
with open("class1.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
totmark=0
totentrys=len(filedata)
for marks in filedata:
    totmark=totmark+float(marks[1])
mean=totmark/totentrys
print("mean is :"+str(mean))
df=pd.read_csv("class1.csv")
fig=px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= mean, y1= mean,
      x0= 0, x1= totentrys
    )
])
fig.update_yaxes(rangemode="tozero")
fig.show()
