import pandas as pd
import matplotlib.pyplot as plt
var=pd.read_csv("Sales_Data_Analyzer/Walmart_Sales.csv")
#drop value
var.dropna()
print(var.dropna())
#fill value
print(var.fillna("ffill"))
print(var.drop_duplicates())
#total_sales
var["Total_Sales"]=var.groupby("CPI")["Weekly_Sales"].transform("sum")
#fuel cost
var["Fuel_cost"] = var["Fuel_Price"].sum()
print(var)
#filter price
print(var["Total_Sales"]>1643690.90 )
plt.subplot(2,2,1)
plt.hist("Total_Sales")
plt.subplot(2,2,2)
plt.scatter("Weekly_Sales","Temperature")
plt.subplot(2,2,3)
plt.hist("Unemployment")
plt.subplot(2,2,4)
plt.scatter("Fuel_cost","Fuel_Price")
plt.show()