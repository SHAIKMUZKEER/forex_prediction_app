import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

df = pd.read_csv("eurusd_hour.csv")
df.head(100)

df.info()

df.isnull().sum()

df["DateTime"] = pd.to_datetime(df["Date"] + " " + df["Time"])
df.head()

df["Date"] = pd.to_datetime(df["Date"])
print(df["Date"].dtype)

df.set_index(df["DateTime"], inplace = True)
df.head()

df.drop(columns = ["DateTime","BCh","ACh","Date","Time"], inplace = True)
df.head()

df["day"] = df.index.day
df["month"] = df.index.month
df["year"] = df.index.year
df["hour"] = df.index.hour
df

df["volatility"] = df["BH"] - df["BL"]   ## volatility is the measurement that is used to show the momentum and the price fluctuation.

## liquidity calculation
df["spread"] = df["AC"] - df["BC"]
df["liquidity"] = 1 / df["spread"]

## smoothing the volitality for best line relation
df["volitality_LAG_1"] = df["volatility"].rolling(window = 168).mean()
df["volitality_LAG_1_24"] = df["volitality_LAG_1"].rolling(window = 168).mean()


plt.figure(figsize = (10,5))

plt.subplot(1,2,1)
plt.plot(df.index , df["volitality_LAG_1"] , label = "time VS volitality")
plt.title("PRESENT VOLITALITY")
plt.grid(True)
plt.legend()

plt.subplot(1,2,2)
plt.plot(df.index , df["volitality_LAG_1_24"] , label = "time VS volitality")
plt.title("PREVIOUS ONE WEEK VOLITALITY")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

## grouping the years
year_group = df.groupby("year")

for i,j in year_group:
  print(i)
  print(j)


plt.figure(figsize = (15,20))

plt.subplot(6,3,1)
plt.plot(year_group.get_group(2005)["liquidity"][:100] , label = "2005")
plt.title("2005 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,2)
plt.plot(year_group.get_group(2006)["liquidity"][:100] , label = "2006")
plt.title("2006 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,3)
plt.plot(year_group.get_group(2007)["liquidity"][:100] , label = "2007")
plt.title("2007 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,4)
plt.plot(year_group.get_group(2008)["liquidity"][:100] , label = "2008")
plt.title("2008 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,5)
plt.plot(year_group.get_group(2009)["liquidity"][:100] , label = "2009")
plt.title("2009 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,6)
plt.plot(year_group.get_group(2010)["liquidity"][:100] , label = "2010")
plt.title("2010 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)



plt.subplot(6,3,7)
plt.plot(year_group.get_group(2011)["liquidity"][:100] , label = "2011")
plt.title("2011 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,8)
plt.plot(year_group.get_group(2012)["liquidity"][:100] , label = "2012")
plt.title("2012 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,9)
plt.plot(year_group.get_group(2013)["liquidity"][:100] , label = "2013")
plt.title("2013 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,10)
plt.plot(year_group.get_group(2014)["liquidity"][:100] , label = "2014")
plt.title("2014 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,11)
plt.plot(year_group.get_group(2015)["liquidity"][:100] , label = "2015")
plt.title("2015 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,12)
plt.plot(year_group.get_group(2016)["liquidity"][:100] , label = "2016")
plt.title("2016 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,13)
plt.plot(year_group.get_group(2017)["liquidity"][:100] , label = "2017")
plt.title("2017 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,14)
plt.plot(year_group.get_group(2018)["liquidity"][:100] , label = "2018")
plt.title("2018 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,15)
plt.plot(year_group.get_group(2019)["liquidity"][:100] , label = "2019")
plt.title("2019 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)


plt.subplot(6,3,16)
plt.plot(year_group.get_group(2020)["liquidity"][:100] , label = "2020")
plt.title("2020 trend")
plt.legend()
plt.xlabel("TIME")
plt.ylabel("LIQUIDITY")
plt.xticks(rotation = 90)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize = (10,6))

sns.scatterplot(x = df["liquidity"][:10000] , y = df["spread"][:10000] , data = df , color = "green" , label = "TREND OF MARKET BUYERS AND SELLERS")
plt.title("LIQUIDITY VS SPREAD")
plt.xlabel("LIQUIDITY")
plt.ylabel("SPREAD")
plt.legend()
plt.show()

df.drop(columns = ["AO","AH","AL","AC","day","month","year","hour","volitality_LAG_1","volitality_LAG_1_24"], inplace = True)

plt.figure(figsize = (10,6))

sns.heatmap(df.corr() , annot = True , cmap = "coolwarm" , cbar = True)

plt.title("relation between all features")
plt.show()


plt.figure(figsize = (6,4))

sns.boxplot(df["BC"] , color = "red")
plt.title("OUTLIER CHECKING")
plt.xlabel("BID  CLOSING PRICE")
plt.show()

df.drop(columns = ["volatility","spread" , "liquidity"], inplace = True)


x = df.drop(columns = ["BC"])
y = df["BC"]

split = int(len(df) * 0.8)

x_train = x[:split]
x_test = x[split:]

y_train = y[:split]
y_test = y[split : ]

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = Ridge(alpha = 0.001)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)


mse = mean_squared_error(y_test , y_pred)
mae = mean_absolute_error(y_test , y_pred)
r2 = r2_score(y_test , y_pred)
rmse = np.sqrt(mean_squared_error(y_test , y_pred))

print("mean_squared_error : " , mse)
print("root_mean_squared_error : " , rmse)
print("mean_absolute_error: ", mae)
print("r2_score : " , r2)


sns.scatterplot(x = y_test[:100] , y = y_pred[:100] , color = "red")
plt.show()


import pickle

# Save model
pickle.dump(model, open("model.pkl", "wb"))

# Save scaler
pickle.dump(scaler, open("scaler.pkl", "wb"))