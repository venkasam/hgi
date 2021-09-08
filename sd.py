import csv
import plotly.express as px
import pandas as pd
import math 
with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
data=filedata[0]
def mean(data):
    n=len(data)
    tot=0
    for x in data:
        tot=tot+int(x)
    mean=tot/n
    return mean

square2=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    square2.append(a)
sum=0
for i in square2:
    sum=sum+i

result=sum/(len(data)-1)
sd=math.sqrt(result)
print(sd)


