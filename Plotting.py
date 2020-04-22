###########################################
############# Last Homework ###############
###########################################

from matplotlib import pylab as plt
import pandas


## Loading TESLA data ##
df1 = pandas.read_csv("TSLA.csv")
df1['Date'] = pandas.to_datetime(df1.Date)
#print(df1.head())
#print(len(df1))
new_df1= df1[['Date', 'Close']].copy()
new_df1= new_df1.rename(columns={'Close': 'Tesla Close'})
#print(new_df1.head())

## Loading VOLKSWAGEN data ##
df2 = pandas.read_csv("VOW.DE.csv")
df2['Date'] = pandas.to_datetime(df2.Date)
#print(df2.head())
#print(len(df2))
new_df2= df2[['Date', 'Close']].copy()
new_df2= new_df2.rename(columns={'Close': 'Volkswagen Close'})
#print(new_df2.head())

## Loading BMW data ##
df3 = pandas.read_csv("BMW.DE.csv")
df3['Date'] = pandas.to_datetime(df3.Date)
#print(df3.head())
#print(len(df3))
new_df3= df3[['Date', 'Close']].copy()
new_df3= new_df3.rename(columns={'Close': 'BMW Close'})
#print(new_df3.head())


## Merging the 3 data sets ##
merged = pandas.merge(new_df1, new_df2, on='Date', how='inner', left_index=True, right_index=True)
merged = pandas.merge(merged, new_df3, on='Date', how='inner', left_index=True, right_index=True)
#print(merged)


## Plotting ##
#merged = merged.sort_values('Date', ascending=True)
plt.plot(merged['Date'], merged['Tesla Close'])
plt.plot(merged['Date'], merged['Volkswagen Close'])
plt.plot(merged['Date'], merged['BMW Close'])
plt.legend(["Tesla", "Volkswagen", "BMW"], loc="upper left")

plt.show()


## Correlation ##
print(merged.corr())


# we can see that there is a positive and bigger correlation between Volkswagen and BMW
# Tesla and Volkswagen are also very slightly positively correlated
# It is interesting that Tesla and BMW are negatively correlated.
