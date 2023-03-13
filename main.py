# import pandas library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read file
df = pd.read_csv("finance_liquor_sales.csv")

# create a scatter plot
x = df['zip_code'].values.tolist()
x = np.asarray(x).astype(int)
y = df['bottles_sold'].values.tolist()
colors = np.random.randint(100, size=len(y))

plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles sold per Zip code')
plt.xticks(rotation=30)
plt.scatter(x, y, c=colors)
plt.show()

# get the most popular item sold based on zip code

# group results by Zip code summing the bottles
zipitem = df.groupby(['zip_code', 'item_description'])
bottles_sold = zipitem.agg({'bottles_sold': 'sum'})

# sort by bottles sold
sort = bottles_sold.sort_values(by="bottles_sold", ascending=False)

# set zip_code as index and remove duplicates keeping the first occurence
distinct = (sort.reset_index()
            .drop_duplicates(subset='zip_code')
            .set_index('zip_code').sort_index())

# print(distinct)

# visualize data with matlib
