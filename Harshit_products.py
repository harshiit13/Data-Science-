import pandas as pd
import numpy as np
import csv

# Dataset
df = pd.read_csv("Sample Dataset for Coding Task.csv")


# List of Category
d= []
for col in df.Category :
  if col not in d:
    d.append(col)


#Pair of Category to Products
c_p = {}
for val in d:
  c_p[val] = []

for i,r in df.iterrows():
  if r[2] not in c_p[r[1]]:
    c_p[r[1]].append(r[2])



# Category and products sales
cate = {}
products = {}
for i,r in df.iterrows():
  cate[r[1]] =cate.get(r[1],0) + df["Sales"][i]
  products[r[2]] = products.get(r[2],0) + df["Sales"][i]



d = []

for c in c_p:
    for p in c_p[c]:
        x = round(products[p] / cate[c] * 100, 2)
        d.append([c, p, x])

c_f = "HARSHIT_PRODUCTS.csv"


h = ["Category", "Product", "Sales Percentage"]


with open(c_f, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(h)  
    writer.writerows(d)   

print("Created HARSHIT_PRODUCTS .... ")